from . import admin
from flask import request, redirect
from webserver.model import DBSession, User, login_manager
from flask.ext.login import login_user, login_required, logout_user


@login_manager.user_loader
def load_user(user_id):
    session = DBSession()
    uid = session.query(User).get(int(user_id))
    session.close()
    return uid


@admin.route('/login', methods=['POST'])
def login():
    print 'post'
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    session = DBSession()
    user = session.query(User).filter_by(name=user_name).first()
    session.close()
    if user is not None and user.verify_password(password):
        login_user(user)
    return redirect('/')


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
