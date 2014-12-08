from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config.from_object('config')
db = SQLAlchemy(app)
  
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    position_x = db.Column(db.Integer)
    position_y = db.Column(db.Integer)
    tweet_id = db.Column(db.BigInteger)

    def __init__(self, date, position_x, position_y, tweet_id):
        self.date = date;
        self.position_x = position_x;
        self.position_y = position_y;
        self.tweet_id = tweet_id

    def __repr__(self):
        return '<Tweet %d>' % self.id


from app import views

import flask.ext.restless

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

@app.route("/api/v1/tweet")
def list_users():
  return "user_example"

tweet_blueprint = manager.create_api(Tweet,
                                     methods=['GET'], results_per_page=100000, max_results_per_page=100000 )