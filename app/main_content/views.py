import os

from flask import Blueprint
from flask import jsonify

blueprint = Blueprint('main_content', __name__, url_prefix='/', static_folder='../static')
endpoint = "https://funny-comic-server.herokuapp.com"


@blueprint.route('/')
def main():
    return jsonify(data=[
        {
            "id": 1,
            "title": "Kim Chi Cu Cai",
            "image": "",
            "link": endpoint + "/kim-chi-cu-cai"
        },
        {
            "id": 2,
            "title": "Gintama",
            "image": "",
            "link": endpoint + "/kim-chi-cu-cai"
        },
        {
            "id": 3,
            "title": "Gintama",
            "image": "",
            "link": endpoint + "/kim-chi-cu-cai"
        },
        {
            "id": 3,
            "title": "Gintama",
            "image": "",
            "link": endpoint + "/kim-chi-cu-cai"
        }
    ])


@blueprint.route("kim-chi-cu-cai")
def content():
    files = os.listdir("app/static/images/full")
    data = []

    for file in files:
        url = endpoint + "/static/images/full/" + file
        data.append({
            'url': url
        })

    return jsonify(data=data)
