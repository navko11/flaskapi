from init import db, ma 
from marshmallow import fields

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Price)

    order = db.relationship("Order", back_populates="items")


class ItemSchema(ma.Schema):
    
    order = fields.Nested('OrderSchema', exclude=["items"])

    class Meta:
        fields = ('id', 'description', 'quantity', 'price', 'order')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)