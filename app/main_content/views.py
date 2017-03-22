from flask import Blueprint
from flask import jsonify

import os

blueprint = Blueprint('main_content', __name__, url_prefix='/', static_folder='../static')
endpoint = "http://localhost:5000"


@blueprint.route('/')
def main():
    return jsonify(data=[
        {
            "id": 1,
            "title": "Kim Chi Cu Cai",
            "image": "",
            "link": endpoint + "1"
        },
        {
            "id": 2,
            "title": "Gintama",
            "image": "",
            "link": ""
        }
    ])


@blueprint.route("abc")
def content():
    files = os.listdir("app/static/images/full")
    data = []

    for file in files:
        url = endpoint + "/static/images/full/" + file
        data.append({
            'url': url
        })

    return jsonify(data=data)
