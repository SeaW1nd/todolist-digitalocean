from flask import Blueprint, request, jsonify, redirect, url_for, render_template, session, flash
from .model import Users, tododb
from flask_login import login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from password_strength import PasswordPolicy
import pyotp
from itsdangerous import URLSafeTimedSerializer
from secrets import token_bytes
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
import uuid


todo = Blueprint('todo', __name__, static_folder='../static/', template_folder='../templates/')

#Endpoints

@todo.route('/todo', methods=['GET'])
@login_required
def main_page():
    curr_user = Users.query.get(current_user.get_id())
    if curr_user.isFillForm == False:
        return redirect(url_for('profiles.profile', type=session['type']))
    else:
        return render_template('mainPage.html')
    
