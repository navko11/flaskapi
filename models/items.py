from init import db, ma 
from marshmallow import fields

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    price = db.Column(db.String)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)

    order = db.relationship("Order", back_populates="items")


class ItemSchema(ma.Schema):
    
    order = fields.Nested('OrderSchema', exclude=['items'])

    class Meta:
        fields = ('id', 'description', 'quantity', 'price', 'order')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)