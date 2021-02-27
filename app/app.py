import random
import hashlib
import string
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf, URL

SECRET_KEY = ''.join(random.choices(
    string.ascii_uppercase + string.digits, k=16))
hashed_secret_key = hashlib.sha256()
hashed_secret_key.update(bytes(SECRET_KEY, encoding='utf-8'))
SECRET_KEY = hashed_secret_key.digest()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

Bootstrap(app)

# hashed_password = hashlib.sha256()
# hashed_password.update(b"This is a")
# hashed_password.update(b" great python tutorial.")
# hashed_password.digest()

class PasswordForm(FlaskForm):
    masterpassword = PasswordField('password', validators=[InputRequired()])
    username = StringField('username', validators=[InputRequired(), Length(6,10)])
    website = StringField('website', validators=[InputRequired(), URL()])

@app.route('/', methods=['POST', 'GET'])
def index():
    form = PasswordForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            masterpassword = form.masterpassword.data
            username = form.username.data
            website = form.website.data
            return("{}{}{}".format(masterpassword, username, website))
    else:
        return render_template("index.html", form=form)


@app.route('/hash', methods=['POST'])
def hash():
    form = PasswordForm()



if __name__ == '__main__':
    app.run(debug=True)
