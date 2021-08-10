from flask import Flask
from mvc_example.views.mvc_views import mvc_blueprint

app = Flask(__name__)

app.register_blueprint(mvc_blueprint, url_prefix="/mvc-example")

# TODO: remove this when more mature
@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

