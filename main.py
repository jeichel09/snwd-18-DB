from flask import Flask, render_template, request, redirect, url_for
from model import User, db

app = Flask(__name__)
db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    user = User(name=name, email=email)
    db.add(user)
    db.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()