from flask import (render_template, url_for, flash, redirect,
                   request, Blueprint)
from flask_blog.main.forms import PhoneNumberValidation
from flask_blog.models import Post
from flask import current_app
import requests

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html',posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/phonevalidation", methods=['GET','POST'])
def phonevalidation():
    form = PhoneNumberValidation()
    if form.validate_on_submit():
        try:
            api_key = current_app.config['NUMVERIFY_API_KEY']
            data=form.phone.data
            response = requests.get(f'http://apilayer.net/api/validate?access_key={api_key}&number={data}&country_code=US')
            if response.status_code !=200:
                return redirect(url_for('main.phonevalidation'))
            data = response.json()
        except requests.exceptions.RequestException as e:
            error = f"Api failed: {e}"
        except ValueError:
            error = "Invalid Response Recieved"
        return render_template('apiresponse.html',title="Api Response",data=data)
    return render_template('phonevalidation.html', title='Phone Validation', form=form)

    
