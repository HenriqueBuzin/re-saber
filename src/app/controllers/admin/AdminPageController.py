from flask import request, redirect, url_for, render_template
from app.models.ppcp import Ppcp

def get():

    warning = request.args.get('warning')

    warning_class = request.args.get('warning_class')

    ppcp_instance = Ppcp()

    existing_ppcps = ppcp_instance.get_all_ppcps_with_names()

    return render_template('admin/admin_page.html', existing_ppcps=existing_ppcps, warning=warning, warning_class=warning_class)

def delete(ppcp_id):

    ppcp_instance = Ppcp()
    delete_result = ppcp_instance.delete_ppcp_by_id(ppcp_id)

    if delete_result:
        warning = 'Documento excluído com sucesso!'
        warning_class='alert-success'
    else:
        warning = 'Documento não encontrado ou não foi excluído.'
        warning_class='alert-danger'

    return redirect(url_for('admin.admin_page', warning=warning, warning_class=warning_class))
