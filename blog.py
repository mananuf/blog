from flask import Flask,render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEYS'] = '5468e77745e8b9a5b55adbf16e9bdb9'


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


@app.route('/registration')
def registration():
    form = RegistrationForm()
    return render_template('register.html', form=form )


@app.route('/login')
def registration():
    form = LoginForm()
    return render_template('login.html', form=form )

if __name__ == "__main__":
    app.run(debug=True)