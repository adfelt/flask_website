from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9ec9f7e76250a1aff186a5d4acc1215c093586fd8d473eb475cf4c351fb9c8f'

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'January 5th, 2024'
    },
    {
        'author':'John Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'January 6th, 2024'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html' title='Register', form = form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html' title='Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)