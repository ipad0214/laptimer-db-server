import simplejson

from flask import Blueprint, request
from entities.user import User
from entities.car import Car
from datetime import datetime


def user_routing(session):
    user_bp = Blueprint('user', __name__)

    @user_bp.route('/user', methods=['GET'])
    def get_rain():
        return get_all_entrys()

    @user_bp.route('/user', methods=['POST'])
    def create_highscore_entry():
        new_user = User(
            name=request.json["name"],
            favorite_car=request.json["favoriteCar"],
        )
        session.add(new_user)
        session.commit()

        return get_all_entrys()

    def get_all_entrys():
        query = session.query(User.id, User.name, Car.name, Car.img).join(Car, Car.id == User.favorite_car)
        test = query.all()
        return test

    def create_time_stamp():
        return datetime.now()

    return user_bp
