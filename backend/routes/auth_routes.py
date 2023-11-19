from flask_login import login_required
from app import db


# Create a route for user login. This route will handle user authentication and redirect users to the appropriate page upon successful login.
@main_routes.route('/protected')
@login_required
def protected_route():
    return render_template('protected.html')


from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from models.user_model import User
from forms import LoginForm, RegistrationForm

user_routes = Blueprint('user', __name__)

@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

@user_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@user_routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('user.login'))

    return render_template('register.html', form=form)
