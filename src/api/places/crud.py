# import json

from src import db
from src.api.places.models import Place


def get_all_places():
    return Place.query.all()


def get_place_by_id(place_id):
    return Place.query.filter_by(id=place_id).first()


def get_place_by_name(place_name):
    # exact name search
    return Place.query.filter_by(name=place_name).first()


def add_place(lat, lon, name, types):
    place = Place(lat=lat, lon=lon, name=name, types=types)
    db.session.add(place)
    db.session.commit()
    return place


def update_place(place, lat, lon, name, types):
    place.coords = f"POINT({lon} {lat})"
    place.name = name
    place.types = types
    db.session.commit()
    return place


def delete_place(place):
    db.session.delete(place)
    db.session.commit()
    return place
