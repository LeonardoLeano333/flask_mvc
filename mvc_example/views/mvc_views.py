from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mvc_blueprint = Blueprint('mvc_example', __name__)

@mvc_blueprint.route('/')
def show():
    return "<p>Hello, World! MVC EXAMPLE PAGE</p>"

