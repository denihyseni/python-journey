from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired , Email ,Length

import email_validator

class LoginForm(FlaskForm):
    email = StringField(label='Email' , validators=[DataRequired(), Email()])
    password = PasswordField(label='Password' , validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label='Log In')

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "tedimaimiri"
email = "admin@email.com"
password= "123456789"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login" ,methods=['POST','GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == email and login_form.password.data == password:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html' , form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
