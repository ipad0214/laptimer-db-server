import simplejson

from flask import Blueprint, request
from entities.highscore import Highscore
from datetime import datetime


def highscore_routing(session):
    highscore_bp = Blueprint('highscore', __name__)

    @highscore_bp.route('/highscore', methods=['GET'])
    def get_rain():
        return get_all_entrys()

    @highscore_bp.route('/highscore', methods=['POST'])
    def create_highscore_entry():
        new_highscore = Highscore(
            name=request.json["name"],
            laptime=request.json["laptime"],
            date=create_time_stamp()
        )
        session.add(new_highscore)
        session.commit()

        return get_all_entrys()

    def get_all_entrys():
        return simplejson.dumps([highscore.serialize for highscore in session.query(Highscore)], indent=2)

    def create_time_stamp():
        return datetime.now()

    return highscore_bp
