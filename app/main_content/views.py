from flask import Blueprint

blueprint = Blueprint('main_content', __name__, url_prefix='/', static_folder='/static')


@blueprint.route('/')
def hello():
    return 'Hello World'

