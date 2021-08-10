from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

from flask import request


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, name):
        self.name = name


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route('/items', methods=['POST'])
def set_items():
    data = request.get_json()
    item_name = data['name']
    db.session.add(Item(name=item_name))
    db.session.commit()
    return json.dumps("Added"), 200


