from flask import request, redirect, url_for, render_template
from app.models.user import User

def get():

    user_instance = User()
    user_count = user_instance.users_count()

    if user_count == 1:
        return redirect(url_for('admin.admin_index_get', warning='Usuário já configurado', warning_class='alert-danger'))
    
    return render_template('admin/config.html')

def post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user_instance = User()

    inserted_id = user_instance.insert_user(email, password)

    return redirect(url_for('admin.admin_index_get', warning='Usuário configurado com sucesso!', warning_class='alert-success'))
