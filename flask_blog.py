from flask import Flask, render_template


app = Flask(__name__)



posts=[

    {
        'author': 'tyrion lannister',
        'title': 'blog post'
    },

    {
        'author': 'dennis',
        'title': 'second breakfast'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("hello.html")


@app.route("/about")
def about():
    return render_template("about.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)