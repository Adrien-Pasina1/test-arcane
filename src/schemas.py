from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'date_birth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class PropertySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'type', 'city', 'rooms', 'char_rooms', 'owner_id')


property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)



