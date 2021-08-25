from flask import Blueprint, render_template, abort

mvc_blueprint = Blueprint('mvc_example', __name__)

@mvc_blueprint.route('/', methods=["GET"])
def show():
    return "<p>Hello, World! MVC EXAMPLE PAGE</p>"

