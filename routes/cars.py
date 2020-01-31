import simplejson

from flask import Blueprint, request
from entities.car import Car


def car_routing(session):
    car_bp = Blueprint('car', __name__)

    @car_bp.route('/car', methods=['GET'])
    def get_rain():
        return get_all_entrys()

    @car_bp.route('/car', methods=['POST'])
    def create_highscore_entry():
        new_user = User(
            name=request.json["name"],
            img=request.json["img"],
        )
        session.add(new_user)
        session.commit()

        return get_all_entrys()

    def get_all_entrys():
        return simplejson.dumps([car.serialize for car in session.query(Car)], indent=2)

    def create_time_stamp():
        return datetime.now()

    return car_bp
