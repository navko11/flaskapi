from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.order import Order
from datetime import date

db_commands = Blueprint('db',__name__)


@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            email="shopadmin@email.com",
            password=bcrypt.generate_password_hash('abcdefg').decode('utf-8'),
            is_admin=True
        ),
        User(
            email="shopstaff@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    
    orders = [
        Order(
            date=date.today(),
            message='Order testing',
            status='Processing',
            user=users[0]
        ),
        Order(
            date=date.today(),
            message='Order testing',
            status='In transit',
            user=users[1]
        ),
        Order(
            date=date.today(),
            message='Order testing',
            status='Delivered',
            user=users[0]
        )
    ]

    db.session.add_all(orders)

    db.session.commit()

    print("Tables seeded")

