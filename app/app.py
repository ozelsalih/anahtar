import random
import hashlib
import string
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf, URL

SECRET_KEY = ''.join(random.choices(
    string.ascii_uppercase + string.digits, k=16))
hashed_secret_key = hashlib.sha256()
hashed_secret_key.update(bytes(SECRET_KEY, encoding='utf-8'))
SECRET_KEY = hashed_secret_key.hexdigest()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

Bootstrap(app)


class PasswordForm(FlaskForm):
    masterpassword = PasswordField('password', validators=[InputRequired()])
    username = StringField('username', validators=[InputRequired()])
    website = StringField('website', validators=[InputRequired()])


@app.route('/')
def index():
    form = PasswordForm()
    return render_template("index.html", form=form)


@app.route('/hash', methods=['POST'])
def hash():
    form = PasswordForm()
    if form.validate_on_submit():
        masterpassword = form.masterpassword.data
        username = form.username.data
        website = form.website.data

    else:
        return request.referrer

    alphabet = string.ascii_letters + string.digits + "-_*$/%}."

    seed = hashlib.sha3_512()
    seed.update(bytes(username, encoding="utf-8"))
    seed.update(bytes(website, encoding="utf-8"))
    seed.update(bytes(masterpassword, encoding="utf-8"))
    seed = seed.hexdigest()

    random.seed(seed)

    password_lenght = random.randint(6, 50)

    password = ''.join(
        map(lambda x: random.choice(alphabet), range(password_lenght)))

    return render_template("hash.html", password=password)


if __name__ == '__main__':
    app.run(debug=True)
