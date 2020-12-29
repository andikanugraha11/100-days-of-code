from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'users'

    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String)
    email           = db.Column(db.String)
    password        = db.Column(db.String)
    salt            = db.Column(db.String)
    created_date    = db.Column(db.Date)
    updated_date    = db.Column(db.Date)
    isVerified      = db.Column(db.Bool)
    role            = db.Column(db.Integer)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)