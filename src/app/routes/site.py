from flask import Blueprint, send_from_directory
from app.controllers.site import (AboutController,
                                  IndexController,
                                  HowToImplementController,
                                  BooksController,
                                  MultimediaController,
                                  PpcpsController,
                                  ExperiencesController,
                                  FaqController)

site = Blueprint('site', __name__, url_prefix='/')

@site.route('/sobre', methods=['GET'])
def about():
    return AboutController.get()

@site.route('/', methods=['GET'])
def index():
    return IndexController.get()

@site.route('/como_implementar', methods=['GET'])
def how_to_implement():
    return HowToImplementController.get()

@site.route('/livros', methods=['GET'])
def books():
    return BooksController.get()

@site.route('/multimedia', methods=['GET'])
def multimedia():
    return MultimediaController.get()

@site.route('/ppcps', methods=['GET'])
def ppcps_get():
    return PpcpsController.ppcps_get()

@site.route('/ppcps', methods=['POST'])
def ppcps_post():
    return PpcpsController.ppcps_post()

@site.route('/ppcp_pdf/<ppcp_id>', methods=['GET'])
def ppcp_get(ppcp_id):
    return PpcpsController.ppcp_get(ppcp_id)

@site.route('/ppcp_file_get/<ppcp_id>', methods=['GET'])
def ppcp_file_get(ppcp_id):
    return PpcpsController.ppcp_file_get(ppcp_id)

@site.route('/experiencias', methods=['GET'])
def experiences():
    return ExperiencesController.get()

@site.route('/faq', methods=['GET'])
def faq():
    return FaqController.get()

@site.route('/infografico_download')
def infografico_download():
    path = 'static/pdfs'
    return send_from_directory(path, 'infografico.pdf', as_attachment=True)
