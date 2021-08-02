from wtforms import Form, StringField, validators as v


class InputForm(Form):

    effect_1 = StringField(
        label='effect_1',
        validators=[v.InputRequired('Please provide desired effect')])

    effect_2 = StringField(
        label='effect_2',
        validators=[v.InputRequired('Please provide desired effect')])

    effect_3 = StringField(
        label='effect_3',
        validators=[v.InputRequired('Please provide desired effect')])
