from flask import Blueprint, request
from marshmallow import ValidationError
from mvc_example.controler.schemas.api_schemas import HelloAPISchema

api_blueprint = Blueprint('api_example', __name__)

@api_blueprint.route('/', methods=["GET","POST"])
def hello_api():
    dict_data = request.get_json()
    schema = HelloAPISchema()
    try:
        cleanead_data = schema.load(dict_data)
    except ValidationError as err:
        return err.messages

    return "Hello " + cleanead_data["name"]