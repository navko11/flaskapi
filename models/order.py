from init import db, ma 
from marshmallow import fields

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    message = db.Column(db.Text)
    status = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='orders')

    items = db.relationship('Item', back_populates="order", cascade='all, delete')

class OrderSchema(ma.Schema):

    user = fields.Nested('UserSchema', only = ['email'])

    items = fields.List(fields.Nested('ItemSchema', exclude=["Order"]))

    class Meta:
        fields = ('id', 'date', 'message', 'status', 'user', 'items')
        ordered = True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)