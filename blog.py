# from wsgiref import validate
# import email
# from email.policy import default
# from enum import unique
from flask import Flask,render_template,url_for,redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
# import os

app = Flask(__name__)




# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY


app.config['SECRET_KEY'] = '5468e77745e8b9a5b55adbf16e9bdb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #setting relative path for sqlite DB


db = SQLAlchemy(app) #creating an instance for DB

class User(db.Model):
    int = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    image_file = db.Column(db.TString(20), nullable=False, default='default.jpg')
    posts = db.Relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.image_file})'


class Post(db.Model):
    int = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.Sting(80), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __repr__(self):
        return f'Post({self.title}, {self.date_posted})'


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