import os

from geoalchemy2 import Geography
from geoalchemy2.shape import to_shape

from src import db


class Place(db.Model):

    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    coords = db.Column(Geography(geometry_type="POINT", srid=4326), nullable=False)
    types = db.Column(db.VARCHAR(255), nullable=False)

    def __init__(self, lat, lon, name, types):
        self.coords = f"POINT({lon} {lat})"
        self.name = name
        self.types = types

    def serialize(self):
        point = to_shape(self.coords)

        return {
            "name": self.name,
            "latitude": point.y,
            "longitude": point.x,
            "type": self.types,
        }


if os.getenv("FLASK_ENV") == "development":
    from src import admin
    from src.api.places.admin import PlacesAdminView

    admin.add_view(PlacesAdminView(Place, db.session))
