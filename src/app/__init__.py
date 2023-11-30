from flask import Flask
from app.routes.site import site
from app.routes.admin import admin
from app.models import mongo
from app.seeders import Seeder
from app.controllers.admin import mail
import os

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

    app.template_folder = 'views'

    app.static_folder = 'static'

    app.register_blueprint(site)

    app.register_blueprint(admin)

    app.config["MONGO_URI"] = (f'mongodb://'
                           f'{os.environ["MONGO_USERNAME"]}'
                           f':{os.environ["MONGO_PASSWORD"]}'
                           f'@{os.environ["MONGO_HOSTNAME"]}:27017'
                           f'/{os.environ["MONGO_DATABASE"]}?authSource=admin')

    mongo.init_app(app)

    seeder = Seeder()
    
    seeder.seed_all_data()
    
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_DEFAULT_SENDER'] = os.environ["EMAIL_USERNAME"]
    app.config['MAIL_USERNAME'] = os.environ["EMAIL_USERNAME"]
    app.config['MAIL_PASSWORD'] = os.environ["EMAIL_PASSWORD"]
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail.init_app(app)

    return app

app = create_app()
