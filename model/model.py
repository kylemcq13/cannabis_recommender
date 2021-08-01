from wtforms import Form, StringField, validators as v


class InputForm(Form):

    Effect_1 = StringField(
        label='Desired Effect #1',
        validators=[v.InputRequired('Please provide desired effect')])

    Effect_2 = StringField(
        label='Desired Effect #2',
        validators=[v.InputRequired('Please provide desired effect')])

    Effect_3 = StringField(
        label='Desired Effect #3',
        validators=[v.InputRequired('Please provide desired effect')])
        