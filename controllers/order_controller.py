from flask import Blueprint
from init import db
from models.order import Order, orders_schema


orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


@orders_bp.route('/')
def get_all_orders():
    stmt = db.select(Order).order_by(Order.date.desc())
    orders = db.session.scalars(stmt)
    return orders_schema.dump(orders)
                            