from flask import Blueprint, request
from init import db
from models.order import Order, orders_schema, order_schema
from models.items import Item, item_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


@orders_bp.route('/')
def get_all_orders():
    stmt = db.select(Order).order_by(Order.date.desc())
    orders = db.session.scalars(stmt)
    return orders_schema.dump(orders)


@orders_bp.route('/<int:order_id>')
def get_order(order_id):
    stmt = db.select(Order).filter_by(id=order_id)
    order = db.session.scalar(stmt)
    if order:
        return order_schema.dump(order)
    else:
        return {"error": f"Order {order_id} does not exist"}, 404
    

@orders_bp.route("/", methods=["POST"])
@jwt_required() #To identify which user id is accessing this route
def create_order():
    body_data = request.get_json()
    order = Order(
        date = date.today(),
        message = body_data.get('message'),
        status = body_data.get('status'),
        user_id = get_jwt_identity()
    )
    db.session.add(order)
    db.session.commit()
    return order_schema.dump(order), 201 


@orders_bp.route("/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    stmt = db.select(Order).where(Order.id == order_id)
    order = db.session.scalar(stmt)
    if order:
        db.session.delete(order)
        db.session.commit()
        return {'message': f"Order {order_id} has been deleted"}
    else:
        return {'error': f"Order {order_id} does not exist"}, 404
    

@orders_bp.route("/<int:order_id>", methods=["PUT", "PATCH"])
def update_order(order_id):
    body_data = request.get_json()
    stmt = db.select(Order).filter_by(id=order_id)
    order = db.session.scalar(stmt)
    if order:
        order.message = body_data.get('message') or order.message
        order.status = body_data.get('status') or order.status
        db.session.commit()
        return order_schema.dump(order)
    else:
        return {"error": f"Order {order_id} does not exist"}, 404
    

@orders_bp.route("<int:order_id>/items", methods=["POST"])
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
    

@orders_bp.route("/<int:order_id>/items/<int:item_id>", methods=["DELETE"])

def delete_item(order_id, item_id):
    stmt = db.select(Item).filter_by(id=item_id)
    item = db.session.scalar(stmt)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Item with id {item_id} has been deleted"}
    else:
        return {"error": f"Item with id {item_id} does not exist"}, 404


@orders_bp.route("/<int:order_id>/items/<int:item_id>", methods=["PUT", "PATCH"])

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

