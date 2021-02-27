import random, hashlib, string
from flask import Flask, render_template, request

SECRET_KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
HASHED_SECRET_KEY = hashlib.sha256()
HASHED_SECRET_KEY.update(bytes(SECRET_KEY, encoding='utf-8'))
SECRET_KEY = HASHED_SECRET_KEY.digest()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

hashed_password = hashlib.sha256()
hashed_password.update(b"This is a")
hashed_password.update(b" great python tutorial.")
hashed_password.digest()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
