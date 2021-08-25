from flask import Flask
from mvc_example.views.mvc_views import mvc_blueprint
from api_example.views.api_views import api_blueprint

app = Flask(__name__)

app.register_blueprint(mvc_blueprint, url_prefix="/mvc-example")
app.register_blueprint(api_blueprint, url_prefix="/api-example")

# TODO: remove this when more mature
@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()