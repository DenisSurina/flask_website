from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config["SECRET_KEY"] = "eec89c0e52dcd5615173ef16fc06e1c2"


posts = [
    {"author": "tyrion lannister", "title": "blog post"},
    {"author": "dennis", "title": "second breakfast"},
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("hello.html")


@app.route("/about")
def about():
    return render_template("about.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():

    form = LoginForm()()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
