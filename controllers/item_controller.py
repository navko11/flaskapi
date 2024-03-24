from flask import Blueprint, request
from init import db
from models.order import Order, orders_schema, order_schema
from models.items import Item, item_schema

from flask_jwt_extended import jwt_required, get_jwt_identity


items_bp = Blueprint('items', __name__, url_prefix="/<int:order_id>/items")



@items_bp.route("/", methods=["POST"])
def create_item(order_id):
    body_data = request.get_json()
    stmt = db.select(Order).filter_by(id=order_id)
    order = db.session.scalar(stmt)
    if order:
        item = Item(
            description = body_data.get('description'),
            quantity = body_data.get('quantity'),
            price = body_data.get('price'),
            order = order,
        )
        db.session.add(item)
        db.session.commit()
        return item_schema.dump(order), 201
    else:
        return {"error": f"Order {order_id} does not exist"}, 404
    

@items_bp.route("<int:item_id>", methods=["DELETE"])

def delete_item(order_id, item_id):
    stmt = db.select(Item).filter_by(id=item_id)
    item = db.session.scalar(stmt)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Item with id {item_id} has been deleted"}
    else:
        return {"error": f"Item with id {item_id} does not exist"}, 404


@items_bp.route("<int:item_id>", methods=["PUT", "PATCH"])

def edit_item(order_id, item_id):
    body_data = request.get_json()
    stmt = db.select(Item).filter_by(id=item_id, order_id=order_id)
    item = db.session.scalar(stmt)
    if item:
        item.description = body_data.get('description') or item.description
        item.quantity = body_data.get('quantity') or item.quantity
        item.price = body_data.get('price') or item.price

        db.session.commit()
        return item_schema.dump(item)
    else:
        return {"error": f"Item {item_id} not found in order {order_id}"}

