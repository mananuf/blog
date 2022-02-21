from flask import Flask,render_template,url_for

app = Flask(__name__)


posts = [ #an array/list of dictionaries, containing blog post
    {
        'title': 'Blog Post 1',
        'author': 'Bankat Man',
        'content': 'first post content',
        'date': '12th February, 2022'
    },
    {
        'title': 'Blog Post 2',
        'author': 'Elizabeth creow',
        'content': 'second post content',
        'date': '18th February, 2022'
    },
    {
        'title': 'Blog Post 3',
        'author': 'Mahnjong seo',
        'content': 'third post content',
        'date': '21st February, 2022'
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html", title = 'About')


if __name__ == "__main__":
    app.run(debug=True)