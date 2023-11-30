from flask import request, redirect, url_for, render_template
from app.models.user import User
from app.controllers.admin import mail, Message
import os
from itsdangerous import URLSafeTimedSerializer

SECRET_KEY = os.environ["SECRET_KEY"]

def generate_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    token = serializer.dumps(email)
    return token

EXPIRATION = 172800  # 172800 segundos = 48 horas

def validate_token(token):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(token, max_age=EXPIRATION)
        return email
    except:
        return None

def reset_password_get():

    warning = request.args.get('warning')

    warning_class = request.args.get('warning_class')

    return render_template('admin/reset_password.html', warning=warning, warning_class=warning_class)

def reset_password_post():
    email = request.form.get('email')
    
    user_instance = User()

    existing_user = user_instance.get_password_by_email(email)

    if existing_user:
        token = generate_token(email)
        reset_url = url_for('admin.confirm_password_get', token=token, _external=True) 
        html_content = generate_email_html(reset_url)

        msg = Message( 'Senha',
                       recipients=[email],
                       html=html_content
                    )
        mail.send(msg)

        return redirect(url_for('admin.reset_password_get', warning='E-mail de redefinição enviado com sucesso!', warning_class='alert-success'))

    return redirect(url_for('admin.reset_password_get', warning='Usuário não encontrado!', warning_class='alert-danger'))

def confirm_password_get(token):

    warning = request.args.get('warning')

    warning_class = request.args.get('warning_class')

    return render_template('admin/confirm_password.html', warning=warning, warning_class=warning_class, token=token)

def confirm_password_post():
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    token = request.form.get('token')

    if password != confirm_password:
        return redirect(url_for('admin.confirm_password_get', warning='As senhas são diferentes!', warning_class='alert-danger', token=token))

    email = validate_token(token)
    if not email:
        return redirect(url_for('admin.confirm_password_get', warning='O link de redefinição de senha é inválido ou expirou!', warning_class='alert-danger', token=token))
    
    user_instance = User()

    update_user = user_instance.update_password_by_email(email, password)    
    if update_user:
        return redirect(url_for('admin.admin_index_get', warning='Senha atualizada com sucesso!', warning_class='alert-success'))

def generate_email_html(reset_url):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
        </head>
        <body style="font-family: 'Titillium Web', sans-serif; text-align: center;">
            <div class="container-fluid">
                <div class="header">
                    <img src="https://i.imgur.com/n7nNONa.png" alt="Cabeçalho" style="width: 100%; display: block; border-radius: 15px 15px 0 0;" />
                </div>
                <div class="body" style="padding: 30px; background-color: #C4C4C4; background-image:linear-gradient(#C4C4C4,#C4C4C4);">
                    <p style="color: #1E3963; font-size: 24px; font-weight: bold; margin-top: 20px;">Clique no botão abaixo para redefinir a senha. Este link tem validade de 48 horas.</p>
                    <a href="{ reset_url }" class="btn" style="display: inline-block; background-color: #FFA500; background-image:linear-gradient(#FFA500,#FFA500); font-size: 24px; border: none; padding: 10px 20px; border-radius: 5px; color: #FFFFFF; cursor: pointer; font-weight: bold; text-decoration: none; margin: 30px 0 30px 0;">Redefinir Senha</a>
                </div>
                <div class="footer">
                    <img src="https://i.imgur.com/DM4OsT2.png" alt="Rodapé" style="width: 100%; display: block; border-radius: 0 0 15px 15px;" />
                </div>
            </div>
        </body>
    </html>
    """
    return html_content
