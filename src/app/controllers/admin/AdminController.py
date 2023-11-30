from flask import render_template, redirect, url_for, request, session
from app.models.user import User

def get():

    warning = request.args.get('warning')

    warning_class = request.args.get('warning_class')
    
    user_instance = User()
    user_count = user_instance.users_count()

    if user_count == 0:
        return redirect(url_for('admin.admin_config_get'))

    return render_template('admin/index.html', warning=warning, warning_class=warning_class)

def post():
    email = request.form.get('email')
    password = request.form.get('password')

    user_instance = User()

    existing_user = user_instance.find_user_by_credentials(email, password)

    if existing_user:
        session['user_id'] = existing_user['_id']
        return redirect(url_for('admin.admin_page'))
    
    return redirect(url_for('admin.admin_index_get', warning='Credenciais inválidas', warning_class='alert-danger'))
