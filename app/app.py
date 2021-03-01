import random
import hashlib
import string
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, Optional
from wtforms.widgets import html5 as h5widgets

SECRET_KEY = ''.join(random.choices(
    string.ascii_uppercase + string.digits, k=16))
hashed_secret_key = hashlib.sha256()
hashed_secret_key.update(bytes(SECRET_KEY, encoding='utf-8'))
SECRET_KEY = hashed_secret_key.hexdigest()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

Bootstrap(app)


class PasswordForm(FlaskForm):
    masterpassword = PasswordField(
        'master password', validators=[InputRequired()])
    username = StringField('username', validators=[InputRequired()])
    website = StringField('website', validators=[InputRequired()])
    numbers = BooleanField("numbers",  validators=[Optional()], default=1)
    special_chars = BooleanField("special characters", validators=[Optional()], default=1)
    password_length = BooleanField("limit password length (default 10-25)", id="password_length",  validators=[Optional()], render_kw={"onclick": "valueChanged()"})
    password_length_min = IntegerField('minimum password length', widget=h5widgets.NumberInput(
        min=0, max=120),  validators=[Optional()], default=10)
    password_length_max = IntegerField('maximum password length', widget=h5widgets.NumberInput(
        min=0, max=120),  validators=[Optional()], default=25)


def generate_password(masterpassword, username, website, alphabet, min_length=10, max_length=25):
    seed = hashlib.sha3_512()
    seed.update(bytes(username, encoding="utf-8"))
    seed.update(bytes(website, encoding="utf-8"))
    seed.update(bytes(masterpassword, encoding="utf-8"))
    seed = seed.hexdigest()

    random.seed(seed)

    password_lenght = random.randint(min_length, max_length)

    password = ''.join(
        map(lambda x: random.choice(alphabet), range(password_lenght)))

    return password

@app.route('/')
def index():
    form = PasswordForm()
    return render_template("index.html", form=form)


@app.route('/hash', methods=['POST', 'GET'])
def hash():
    if request.method == 'POST':
        alphabet = string.ascii_letters
        digits = string.digits
        chars = "!\"#$%&'()*+,-./:;<?@[\]^_`{|}~"

        form = PasswordForm()
        if form.validate_on_submit():
            masterpassword = form.masterpassword.data
            username = form.username.data
            website = form.website.data
            numbers = form.numbers.data
            special_chars = form.special_chars.data
            password_lenght = form.password_length.data
            password_length_min = form.password_length_min.data
            password_length_max = form.password_length_max.data

        else:
            return redirect(request.referrer)
        
        if not password_lenght:
            password_length_min = 10
            password_length_max = 25
        
        if numbers:
            alphabet = alphabet + digits

        if special_chars:
            alphabet = alphabet + chars

        password = generate_password(
                masterpassword, username, website, alphabet, password_length_min, password_length_max)
        
        return render_template("hash.html", password=password)

    else:
        return redirect('/')
