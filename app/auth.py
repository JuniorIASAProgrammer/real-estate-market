from flask import Blueprint, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "<p>Log-in</p>"

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p>Log-out</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    return "<p>Sign-up</p>"