# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from datetime import date

home = Blueprint('home', __name__,
                 template_folder='templates')


@home.route('/')
def show():
    try:
        return render_template('base.html', year=date.today().year)
    except TemplateNotFound:
        abort(404)
