from flask import Blueprint
from flask import current_app as app
from flask import jsonify

from app.model import ImageItem

blueprint = Blueprint('main_content', __name__, url_prefix='/', static_folder='../static')


@blueprint.route('/')
def main():
    endpoint = app.config.get("ENDPOINT")
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
            "y": endpoint + "/kim-chi-cu-cai"
        }
    ])


@blueprint.route("kim-chi-cu-cai")
def content():
    items = ImageItem.query.all()
    endpoint = app.config.get("ENDPOINT")

    data = []
    for item in items:
        url = endpoint + "/static/images/" + item.filename
        data.append({
            'origin_url': item.url,
            'url': url,
            'id': item.id,
            'title': item.title
        })

    return jsonify(data=data)
