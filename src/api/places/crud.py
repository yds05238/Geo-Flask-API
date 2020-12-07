# import json

from src import db
from src.api.places.models import Place
# from sqlalchemy.sql import select


# def success_response(data, code=200):
#     return json.dumps({"success": True, "data": data}), code


# def failure_response(message, code=404):
#     return json.dumps({"success": False, "error": message}), code


# def get_all_places():
#     return success_response([t.serialize() for t in Place.query.all()])


# def get_place_by_id(place_id):
#     pl = Place.query.filter_by(id=place_id).first()
#     if pl is None:
#         return failure_response("Place not found")
#     return success_response([pl.serialize()])


# def get_place_by_name(place_name):
#     # exact name search
#     pl = Place.query.filter_by(name=place_name).first()
#     if pl is None:
#         return failure_response("Place not found")
#     return success_response([pl.serialize()])


# def search_places_by_name(place_name):
#     # similar name search
#     s = "%"+place_name + "%"
#     return success_response([t.serialize() for t in Place.query.filter_by(Place.name.like(s)).all()])


# def add_place(lat, lon, name, typ):
#     place = Place(lat=lat, lon=lon, name=name, typ=typ)
#     db.session.add(place)
#     db.session.commit()
#     return place


# def update_place(place, lat, lon, name, typ):
#     # place.update(coords=f"POINT({lon} {lat})", name=name, typ=typ)
#     place.coords = f"POINT({lon} {lat})"
#     place.name = name
#     place.typ = typ
#     db.session.commit()
#     return place


# def delete_place(place):
#     db.session.delete(place)
#     db.session.commit()
#     return place


def get_all_places():
    return Place.query.all()


def get_place_by_id(place_id):
    return Place.query.filter_by(id=place_id).first()


def get_place_by_name(place_name):
    # exact name search
    return Place.query.filter_by(name=place_name).first()
    # pl = Place.query.filter_by(name=place_name).first()
    # if pl is None:
    #     return failure_response("Place not found")
    # return success_response([pl.serialize()])


# def search_places_by_name(place_name):
#     # similar name search
#     s = "%"+place_name + "%"
#     return success_response([t.serialize() for t in Place.query.filter_by(Place.name.like(s)).all()])


def add_place(lat, lon, name, types):
    place = Place(lat=lat, lon=lon, name=name, types=types)
    db.session.add(place)
    db.session.commit()
    return place


def update_place(place, lat, lon, name, types):
    # place.update(coords=f"POINT({lon} {lat})", name=name, typ=typ)
    place.coords = f"POINT({lon} {lat})"
    place.name = name
    place.types = types
    db.session.commit()
    return place


def delete_place(place):
    db.session.delete(place)
    db.session.commit()
    return place
