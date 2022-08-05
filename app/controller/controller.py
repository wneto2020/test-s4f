from app import db
from ..model.models import Vehicle
from flask import request, jsonify


def post_vehicle():
    data_json = request.get_json()
    data = request.get_data()
    vehicle_exist = False

    try:
        vehicle_exist = Vehicle.query.filter(Vehicle.chassi == data_json['chassi']).one()

    except:
        pass

    if not vehicle_exist:
        try:
            db.session.add(data)
            db.session.commit()
            return {"message": "Successfully registered"}, 201

        except:
            return jsonify({'message': 'Unable to create', 'data': {}}), 500

    return jsonify({'message': "vehicle already exists"}), 500


def update_vehicle():
    chassi = request.json['chassi']
    vehicle = Vehicle.query.filter(Vehicle.chassi == chassi).one()

    if not vehicle:
        return jsonify({"message": "vehicle don't exist"})
    try:
        vehicle.ports_number = request.json['ports_number']
        vehicle.color = request.json['color']
        db.session.commit()
        return jsonify({'message': "Successfully updated"}), 201

    except:
        return jsonify({'message': 'Unable to update', 'data': {}}), 500


def delete_vehicle():
    chassi = request.json['chassi']
    vehicle = Vehicle.query.filter(Vehicle.chassi == chassi).one()

    if not vehicle:
        return jsonify({"message": "vehicle don't exist"})
    try:
        db.session.delete(vehicle)
        db.session.commit()
        return jsonify({'message': "Successfully deleted"}), 201

    except:
        return jsonify({'message': 'Unable to deleted', 'data': {}}), 500


def get_vehicle():
    created_at = request.json['created_at']

    if not created_at:
        all_vehicle = Vehicle.query.filter.all()

        return jsonify({'message': 'Successfully request', 'data': all_vehicle}), 200

    try:
        vehicle = Vehicle.query.filter(Vehicle.created_at == created_at)
        return jsonify({'message': 'Successfully request', 'data': vehicle}), 200

    except Exception as err:
        return jsonify(({"message": 'An error has occurred', 'data': err}))


