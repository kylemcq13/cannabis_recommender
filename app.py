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
    
    form = InputForm(request.form)
    if flask.request.method == 'POST' and form.validate():
        result_final = effects_reco(form.Effect_1.data, form.Effect_2.data,
                                    form.Effect_3.data, df)
        m_name = flask.request.form['cleaned_effects']  # Strain should be defined in index.html
        m_name = m_name.title()
        if m_name not in all_effects:
            return(flask.render_template('negative.html', name=m_name))
        else:
            # result_final = effects_reco(m_name)
            strain = []
            type = []
            flavor = []  
            description = []
            for i in range(len(result_final)):
                strain.append(result_final.iloc[i][0])
                type.append(result_final.iloc[i][1])
                flavor.append(result_final.iloc[i][2])
                description.append(result_final.iloc[i][3])

            return flask.render_template(
                                          'positive.html', strain=strain,
                                          type=type,
                                          flavor=flavor,
                                          description=description
                                          )  # all variables here should be defined in the postive.html page


if __name__ == '__main__':
    app.run()
