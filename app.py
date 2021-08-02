import flask
from flask import request
import pandas as pd
from model.model import InputForm
from compute import effects_reco

app = flask.Flask(__name__, template_folder='html_templates')

df = pd.read_csv('data/cannabis.csv')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        form = InputForm(request.form)
        result_final = effects_reco(form.effect_1.data, form.effect_2.data,
                                    form.effect_3.data, df)
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
        


if __name__ == '__main__':
    app.run()
