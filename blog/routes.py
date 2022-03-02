from flask import render_template,url_for,redirect, flash
from blog.forms import RegistrationForm, LoginForm
from blog import app, bcrypt, db
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user

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
    # check for currently loged in account 
    if current_user.is_authenticated: #if the user is already logged in
        return redirect(url_for('home')) #remain in the home page


    form = RegistrationForm()


    if form.validate_on_submit(): #if the form validates correctly,

        # aHasshing and adding to DB 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #hash function
        user = User(username = form.username.data, email=form.email.data, password=hashed_password) # instantiating user DB model
        db.session.add(user) #add to database
        db.session.commit() #save to database

        flash(f'Account for {form.username.data} has been created! You can now login', 'success') #print this success flash

        return redirect(url_for('login')) 

    return render_template('register.html',title ='Register', form=form )


@app.route('/login', methods=['Get','POST'])
def login():

    # check for currently loged in account 
    if current_user.is_authenticated: #if the user is already logged in
        return redirect(url_for('home')) #remain in the home page


    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() #check for email in DB
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if it exists and password matches
            login_user(user, remember=form.remember.data) #log user in and remeber choice

            return redirect(url_for('home'))
        else: #if credentials do not match
            flash(f'Login unsuccessful. check {form.email.data} and password.', 'danger') #flash this

    return render_template('login.html', title='Login', form=form)


# log out route
@app.route('/logout' )
def logout():
    logout_user() #logs the user out
    return redirect(url_for(home)) #returns to home for [login|register]