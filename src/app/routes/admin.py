from flask import Blueprint, redirect, url_for, session
from functools import wraps
from app.controllers.admin import (AdminController, 
                                   AdminPageController,
                                   ConfigAdminController,
                                   RegisterController,
                                   ResetPasswordController)

admin = Blueprint('admin', __name__, url_prefix='/admin')

def require_login(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('admin.admin_index_get'))
        return view(*args, **kwargs)
    return wrapped_view

@admin.route('/', methods=['GET'])
def admin_index_get():
    return AdminController.get()

@admin.route('/', methods=['POST'])
def admin_index_post():
    return AdminController.post()

@admin.route('/configuracao', methods=['GET'])
def admin_config_get():
    return ConfigAdminController.get()

@admin.route('/configuracao', methods=['POST'])
def admin_config_post():
    return ConfigAdminController.post()

@admin.route('/pagina_administrativa', methods=['GET'])
@require_login
def admin_page():
    return AdminPageController.get()

@admin.route('/registrar', methods=['GET'])
@require_login
def register_get():
    return RegisterController.get()

@admin.route('/registrar', methods=['POST'])
@require_login
def register_post():
    return RegisterController.post()

@admin.route('/sair', methods=['GET'])
@require_login
def admin_logout():
    session.clear()
    return redirect(url_for('admin.admin_index_get', warning='Logout realizado com sucesso!', warning_class='alert-success'))

@admin.route('/excluir/<ppcp_id>', methods=['GET'])
@require_login
def delete_ppcp(ppcp_id):
    return AdminPageController.delete(ppcp_id)

@admin.route('/editar/<ppcp_id>', methods=['GET'])
@require_login
def edit_ppcp_get(ppcp_id):
    return RegisterController.edit_get(ppcp_id)

@admin.route('/editar/<ppcp_id>', methods=['POST'])
@require_login
def edit_ppcp_post(ppcp_id):
    return RegisterController.edit_post(ppcp_id)

@admin.route('/recuperar_senha', methods=['GET'])
def reset_password_get():
    return ResetPasswordController.reset_password_get()

@admin.route('/recuperar_senha', methods=['POST'])
def reset_password_post():
    return ResetPasswordController.reset_password_post()

@admin.route('/confirmar_senha/<token>', methods=['GET'])
def confirm_password_get(token):
    return ResetPasswordController.confirm_password_get(token)

@admin.route('/confirmar_senha', methods=['POST'])
def confirm_password_post():
    return ResetPasswordController.confirm_password_post()

@admin.route('/autocomplete/offering_institution', methods=['POST'])
@require_login
def autocomplete_offering_institution_post():
    return RegisterController.autocomplete_offering_institution_post()

@admin.route('/autocomplete/occupation_training', methods=['POST'])
@require_login
def autocomplete_occupation_training_post():
    return RegisterController.autocomplete_occupation_training_post()
