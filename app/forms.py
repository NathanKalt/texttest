from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content")
    prepared = TextAreaField("Prepared")
    trigrams = TextAreaField("Trigrams")
    update = SubmitField("SAVE CHANGES")


class TranslateFrom(FlaskForm):
    title = StringField("Initial text", validators=[DataRequired()])
    content = TextAreaField("Content")
    translated = TextAreaField("Translated")


