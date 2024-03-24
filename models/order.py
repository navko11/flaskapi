from marshmallow import fields
from marshmallow.validate import Length, OneOf
from init import db, ma 

VALID_STATUSES= ("processing", "despatched", "in transit", "delayed", "delivered") 

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    message = db.Column(db.String)
    status = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='orders')

    items = db.relationship('Item', back_populates="order", cascade='all, delete')

class OrderSchema(ma.Schema):

    message = fields.String(required=True, validate=Length(min=2, error="message needs more than 2 characters"))

    status = fields.String(validate=OneOf(VALID_STATUSES))

    user = fields.Nested('UserSchema', only = ['email'])

    items = fields.List(fields.Nested('ItemSchema', exclude=["order"]))

    class Meta:
        fields = ('id', 'date', 'message', 'status', 'user', 'items')
        ordered = True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)