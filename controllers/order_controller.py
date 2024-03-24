from flask import Blueprint, request
from init import db
from models.order import Order, orders_schema, order_schema
from models.items import Item, item_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.item_controller import items_bp


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')
orders_bp.register_blueprint(items_bp)


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
    body_data = order_schema.load(request.get_json()) 
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
    body_data = order_schema.load(request.get_json(), partial=True) #To allow other updates without requiring message
    stmt = db.select(Order).filter_by(id=order_id)
    order = db.session.scalar(stmt)
    if order:
        order.message = body_data.get('message') or order.message
        order.status = body_data.get('status') or order.status
        db.session.commit()
        return order_schema.dump(order)
    else:
        return {"error": f"Order {order_id} does not exist"}, 404
    