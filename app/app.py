import random
import hashlib
import string
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional
from wtforms.widgets import html5 as h5widgets

SECRET_KEY = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
hashed_secret_key = hashlib.sha256()
hashed_secret_key.update(bytes(SECRET_KEY, encoding="utf-8"))
SECRET_KEY = hashed_secret_key.hexdigest()

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

Bootstrap(app)


class PasswordForm(FlaskForm):
    masterpassword = PasswordField("master password", validators=[InputRequired()])
    username = StringField("username", validators=[InputRequired()])
    website = StringField("website", validators=[InputRequired()])
    numbers = BooleanField("numbers", validators=[Optional()], default=1)
    special_chars = BooleanField(
        "special characters", validators=[Optional()], default=1
    )
    password_length = BooleanField(
        "limit length (default 10-25)",
        id="password_length",
        validators=[Optional()],
        render_kw={"onclick": "valueChanged()"},
    )
    password_length_min = IntegerField(
        "minimum length",
        widget=h5widgets.NumberInput(min=8, max=120),
        validators=[Optional()],
        default=10,
    )
    password_length_max = IntegerField(
        "maximum length",
        widget=h5widgets.NumberInput(min=8, max=120),
        validators=[Optional()],
        default=25,
    )


def generate_unicode(masterpassword):
    unicode_icon = "★✓⚐✎✗♡♤♧♘♗♖♔✙❆△♫♪♲"
    mastepassword_as_unicode = ""

    seed = hashlib.sha3_512()
    seed.update(bytes(masterpassword, encoding="utf-8"))

    mastepassword_as_unicode = "".join(
        map(lambda x: random.choice(unicode_icon), range(3))
    )

    return mastepassword_as_unicode


def generate_password(
    masterpassword,
    username,
    website,
    numbers,
    special_chars,
    min_length=10,
    max_length=25,
):
    alphabet = string.ascii_letters
    digits = string.digits
    chars = "!\"#$%&'()*+-./:;<?@[\]^_`{|}"
    password = ""

    sha3 = hashlib.sha3_512()
    sha3.update(bytes(username, encoding="utf-8"))
    sha3.update(bytes(website, encoding="utf-8"))
    sha3.update(bytes(masterpassword, encoding="utf-8"))
    sha3 = sha3.hexdigest()

    blake2s = hashlib.blake2s()
    blake2s.update(bytes(sha3, encoding="utf-8"))
    blake2s = blake2s.hexdigest()

    md5 = hashlib.md5()
    md5.update(bytes(blake2s, encoding="utf-8"))

    seed = md5.hexdigest()

    random.seed(seed)

    password_lenght = random.randint(min_length, max_length)

    if numbers:
        password += "".join(map(lambda x: random.choice(digits), range(3)))
        password_lenght -= 3

    if special_chars:
        password += "".join(map(lambda x: random.choice(chars), range(3)))
        password_lenght -= 3

    password += "".join(map(lambda x: random.choice(alphabet), range(password_lenght)))
    password = "".join(random.sample(password, len(password)))

    return password


@app.route("/")
def index():
    form = PasswordForm()
    return render_template("index.html", form=form)


@app.route("/hash", methods=["POST", "GET"])
def hash():
    if request.method == "POST":

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

        password = generate_password(
            masterpassword,
            username,
            website,
            numbers,
            special_chars,
            password_length_min,
            password_length_max,
        )

        mastepassword_as_unicode = generate_unicode(masterpassword)

        return render_template(
            "hash.html", password=password, unicode=mastepassword_as_unicode
        )

    else:
        return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500