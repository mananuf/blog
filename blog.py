from flask import Flask,render_template,url_for,redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post
# import os

app = Flask(__name__)




# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY


app.config['SECRET_KEY'] = '5468e77745e8b9a5b55adbf16e9bdb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #setting relative path for sqlite DB


db = SQLAlchemy(app) #creating an instance for DB



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


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit(): #if the form validates correctly,
        flash(f'Account for {form.username.data} has been created!', 'success') #print this success flash

        return redirect(url_for('home')) 

    return render_template('register.html',title ='Register', form=form )


@app.route('/login', methods=['Get','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Logged in successfully. Welcome onboard {form.email.data}', 'success')

        return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)