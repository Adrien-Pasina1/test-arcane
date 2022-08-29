from flask import Blueprint, request, jsonify
from src.models import Property, db
from src.schemas import properties_schema, property_schema

property_bp = Blueprint('property_bp', __name__)

@property_bp.route('/properties', methods=['GET'])
def get_properties_by_city_name():
    city = request.args.get('city')
    if city:
        all_properties = Property.query.filter_by(city=city.lower()).all()
        result = properties_schema.dump(all_properties)
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Enter city name as query parameter to search the property'})


@property_bp.route('/properties/<int:user_id>', methods=['POST'])
def add_property(user_id):
    name = request.json['name']
    description = request.json['description']
    type = request.json['type']
    city = request.json['city']
    rooms = request.json['rooms']
    char_rooms = request.json['char_rooms']
    owner_id = user_id

    new_property = Property(name, description, type, city.lower(), rooms, char_rooms, owner_id)

    db.session.add(new_property)
    db.session.commit()
    return property_schema.jsonify(new_property)


@property_bp.route('/properties/<int:user_id>/<int:property_id>', methods=['PUT'])
def update_property(user_id, property_id):
    property = Property.query.filter_by(id=property_id, owner_id=user_id).first()
    print(property)
    if property:
        name = request.json['name']
        city = request.json['city']
        description = request.json['description']
        rooms = request.json['rooms']
        char_rooms = request.json['char_rooms']
        type = request.json['type']

        property.name = name
        property.city = city
        property.description = description
        property.rooms = rooms
        property.char_rooms = char_rooms
        property.type = type

        db.session.commit()

        return property_schema.jsonify(property)
    else:
        return jsonify({"Error": "Could not find the property to update"})



