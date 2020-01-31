from flask import Flask
from routes.highscore import highscore_routing
from routes.user import user_routing
from routes.cars import car_routing

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

db_local_string = "postgresql+psycopg2://postgres:postgres@localhost:5432/laptimer"
db_pi_string = "postgresql+psycopg2://xx:xxxx@192.168.2.143:5432/weatherstation"

db_string = db_local_string
db = create_engine(db_string)
Session = sessionmaker(bind=db)
session = Session()

meta = MetaData(db)

app = Flask(__name__)
highscore_routing = highscore_routing(session)
cars_routing = car_routing(session)
user_routing = user_routing(session)


app.register_blueprint(highscore_routing)
app.register_blueprint(cars_routing)
app.register_blueprint(user_routing)

def main():
    db.connect()
    app.run(debug=False, host='0.0.0.0')


if __name__ == '__main__':
    main()