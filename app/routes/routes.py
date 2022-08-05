from app import app
from ..controller import controller
from flask import render_template

@app.route('/', methods=['GET'])
def get_home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post_vehicle():
    return controller.post_vehicle


@app.route("/", methods=["POST", 'GET'])
def get_vehicle():
    return controller.get_vehicle()


@app.route("/", methods=["PUT"])
def update_vehicle():
    return controller.update_vehicle()


@app.route("/", methods=["DELETE"])
def delete_vehicle():
    return controller.delete_vehicle()


