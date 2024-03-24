from init import db, ma
from marshmallow import fields 

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    orders = db.relationship('Order', back_populates="user", cascade='all, delete')


#Schema to deserialize
    
class UserSchema(ma.Schema):

    orders = fields.Nested('CardSchema', exclude=['User'])

    class Meta:
        fields = ('id', 'email', 'password', 'is_admin')


user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])

