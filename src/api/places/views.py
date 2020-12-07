from flask import request
from flask_restx import Namespace, Resource, fields


from src.api.places.crud import (  # isort:skip
    get_all_places,
    get_place_by_id,
    get_place_by_name,
    add_place,
    update_place,
    delete_place,
)

places_namespace = Namespace("places")


place = places_namespace.model(
    "Place",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "coords": fields.String(required=True),
        "types": fields.String(required=True),
    },
)


class PlacesList(Resource):
    @places_namespace.marshal_with(place, as_list=True)
    def get(self):
        """Returns all places."""
        return get_all_places(), 200

    @places_namespace.expect(place, validate=True)
    @places_namespace.response(201, "<place_name> was added!")
    @places_namespace.response(400, "Sorry. That place already exists.")
    def post(self):
        """Creates a new place."""
        post_data = request.get_json()
        lon = post_data.get("lon")
        lat = post_data.get("lat")
        name = post_data.get("name")
        types = post_data.get("types")
        response_object = {}

        place = get_place_by_name(name)
        if place:
            response_object["message"] = "Sorry. That place already exists."
            return response_object, 400

        add_place(lat, lon, name, types)

        response_object["message"] = f"{name} was added!"
        return response_object, 201


class Places(Resource):
    @places_namespace.marshal_with(place)
    @places_namespace.response(200, "Success")
    @places_namespace.response(404, "Place <place_name> does not exist")
    def get(self, place_id):
        """Returns a single place."""
        place = get_place_by_id(place_id)
        if not place:
            places_namespace.abort(404, f"Place {place_id} does not exist")
        return place, 200

    @places_namespace.expect(place, validate=True)
    @places_namespace.response(200, "<place_id> was updated!")
    @places_namespace.response(400, "Sorry. That place already exists.")
    @places_namespace.response(404, "Place <place_id> does not exist")
    def put(self, place_id):
        """Updates a place."""
        post_data = request.get_json()
        lat = post_data.get("lat")
        lon = post_data.get("lon")
        name = post_data.get("name")
        types = post_data.get("types")
        response_object = {}

        place = get_place_by_id(place_id)
        if not place:
            places_namespace.abort(404, f"Place {place_id} does not exist")

        if get_place_by_name(name):
            response_object["message"] = "Sorry. That place already exists."
            return response_object, 400

        update_place(place, lat, lon, name, types)

        response_object["message"] = f"{place.id} was updated!"
        return response_object, 200

    @places_namespace.response(200, "<place_id> was removed!")
    @places_namespace.response(404, "Place <place_id> does not exist")
    def delete(self, place_id):
        """"Deletes a place."""
        response_object = {}
        place = get_place_by_id(place_id)

        if not place:
            places_namespace.abort(404, f"Place {place_id} does not exist")

        delete_place(place)

        response_object["message"] = f"{place.name} was removed!"
        return response_object, 200


places_namespace.add_resource(PlacesList, "")
places_namespace.add_resource(Places, "/<int:place_id>")
