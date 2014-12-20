# -*- coding: utf-8 -*-

from flask import Flask
from beatmatic import config
from beatmatic.frontend import home


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # set up your database
    # app.engine = create_engine(database_uri)

    # add your modules
    app.register_blueprint(home)

    # other setup tasks

    return app

app = create_app()
