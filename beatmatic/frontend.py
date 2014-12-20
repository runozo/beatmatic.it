# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__,
                 template_folder='templates')


@home.route('/')
def show():
    try:
        return render_template('base.html')
    except TemplateNotFound:
        abort(404)
