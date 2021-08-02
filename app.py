import flask
from flask import request
import pandas as pd
from model.model import InputForm
from compute import effects_reco

app = flask.Flask(__name__, template_folder='html_templates')

df = pd.read_csv('data/cannabis.csv')

all_effects = [df['cleaned_effects'][i] for i in range(len(df['cleaned_effects']))]


# Set up the main route
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # result_final = effects_reco(form.Effect_1.data, form.Effect_2.data,
        #                            form.Effect_3.data, df)
        # m_name = flask.request.form['cleaned_effects']  # Strain should be defined in index.html
        # m_name = m_name.title()
        # if m_name not in all_effects:
        #    return(flask.render_template('negative.html', name=m_name))
        #else:
        form = InputForm(request.form)
        result_final = effects_reco(form.Effect_1.data, form.Effect_2.data,
                                    form.Effect_3.data, df)
        strain = []
        type = []
        flavor = []  
        description = []
        for i in range(len(result_final)):
            strain.append(result_final.iloc[i][0])
            type.append(result_final.iloc[i][1])
            flavor.append(result_final.iloc[i][2])
            description.append(result_final.iloc[i][3])

        return (flask.render_template(
                                 'positive.html', 
                                 canna_strain=strain,
                                 canna_type=type,
                                 canna_flavor=flavor,
                                 canna_desc=description))
        # all variables here should be defined in the positive.html page


if __name__ == '__main__':
    app.run()
