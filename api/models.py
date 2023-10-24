import enum
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class ConservationStatus(enum.Enum):
    extinct = 0
    endangered = 1
    threatened =2
    near_threatened = 3
    observed = 4
    accepted = 5

class Reptile(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(250))
    scientific_name = db.Column(db.String(250))
    native_habitat = db.Column(db.String(250))
    fun_fact = db.Column(db.Text())
    conservation_status = db.Column(db.Enum(ConservationStatus))
    # photo = db.Column(db.String(512))