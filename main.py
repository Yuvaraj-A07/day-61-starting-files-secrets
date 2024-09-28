from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, AnyOf, Length
from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),
                                                   Email()
                                                   ])
    password = PasswordField(label='Password', validators=[DataRequired(),
                                                           Length(max=8,
                                                                  message="Field must be at least 8 characters ")
                                                           ])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "Yuvaraj"
bootstarp = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", forms=form)


if __name__ == '__main__':
    app.run(debug=True)
