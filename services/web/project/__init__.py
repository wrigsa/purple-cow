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
    return jsonify(hello="world")

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
    data = request.get_json()
    item_name = data['name']
    db.session.add(Item(name=item_name))
    db.session.commit()
    return json.dumps("Added"), 200
    
