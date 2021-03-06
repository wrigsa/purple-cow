from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

from flask import request


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name


@app.route("/")
def hello_world():
    return jsonify(hello="fearless")

@app.route('/items', methods=['POST', 'GET', 'DELETE'])
def set_fetch_delete_items():
    if request.method == 'POST':
        db.session.query(Item).delete()
        db.session.commit()
        json_array = json.loads(request.data)
        for item in json_array:
            db.session.add(Item(name=item['name']))
            db.session.commit()
        return json.dumps("Set"), 200

    elif request.method == 'GET':
        items = Item.query.all()
        all_items = []
        for item in items:
            new_item = {
                "id": item.id,
                "name": item.name
            }

            all_items.append(new_item)

        return json.dumps(all_items), 200

    elif request.method == 'DELETE':
        db.session.query(Item).delete()
        db.session.commit()
        return json.dumps("Deleted"), 200

@app.route("/items/add", methods=['POST'])
def add_item():
    data = json.loads(request.data)
    json_array = json.loads(request.data)
    for item in json_array:
        db.session.add(Item(name=item['name']))
        db.session.commit()
    return json.dumps("Added"), 200

@app.route("/items/<id>", methods=['DELETE','PUT','GET'])
def add_modify_fetch_delete_item(id):
    if request.method == 'GET':
        item = Item.query.get(id)
        if (item):
            new_item = {
                "id": item.id,
                "name": item.name
            }
            return json.dumps(new_item), 200
        else:
            return json.dumps("Error: Entry with id {} does not exist".format(id)), 404

    elif request.method == 'PUT':
        data = json.loads(request.data)
        name = data['name']
        item = Item.query.get(id)
        if (item):
            item.name = name
            db.session.commit()
            return json.dumps("Edited"), 200
        else:
            return json.dumps("Error: Entry with id {} does not exist".format(id)), 404
    elif request.method == 'DELETE':
        item = Item.query.get(id)
        if (item):
            db.session.query(Item).filter_by(id=id).delete()
            db.session.commit()
            return json.dumps("Deleted"), 200
        else:
            return json.dumps("Error: Entry with id {} does not exist".format(id)), 404

