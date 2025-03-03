from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message="Name is required."),
        Length(min=2, max=50, message="Name must be between 2 and 50 characters.")
    ])
    email = StringField('Email', validators=[
        DataRequired(message="Email is required."),
        Email(message="Invalid email address.")
    ])
    subject = StringField('Subject', validators=[
        DataRequired(message="Subject is required."),
        Length(min=5, max=100, message="Subject must be between 5 and 100 characters.")
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(message="Message is required."),
        Length(min=10, max=500, message="Message must be between 10 and 500 characters.")
    ])
    submit = SubmitField('Send Message')