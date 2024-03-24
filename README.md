T2A2 - API WEBSERVER PROJECT - Mark Navarro
___________________________________________


R1. Identification of the problem you are trying to solve by building this particular app.

The concept of the app is an online shop where the app will:

- Create information such as users and orders
- Update current orders and their status accordingly
- Delete records when appropriate to prevent any redundant information

___________________________________________
R2. Why is it a problem that needs solving?

Many apps share the same concept of an online shop, and one of the problems is that some of the apps may be difficult to use, store alot of redundant information and apply no normalization, etc.
A good app should be an app that makes information easy to record and easy to collect and read.

___________________________________________
R3. Why have you chosen this database system. What are the drawbacks compared to others?

I have chosen this database system for the reason that many businesses are outdated and still keep records by writing in books.
This database system proves to be more effecient, safe and manageable.

The drawbacks for example, may be the maintenance required to keep the database up to date and the security to protect the information

___________________________________________
R4. Identify and discuss the key functionalities and benefits of an ORM

The functionalities of an ORM is that it takes objects in code and connects them to the database.
The benefits of an ORM helps developers to to handle CRUD operations without using the use of SQL queries.
When interacting with the database it is also more optimized while using an ORM, making the work more smooth and efficient.

___________________________________________
R5. Document all endpoints for your API

order controller
GET/orders
This initial request will return the data that was seeded in the database

```[
	{
		"id": 1,
		"date": "2024-03-24",
		"message": "Order testing",
		"status": "Processing",
		"user": {
			"email": "shopadmin@email.com"
		},
		"items": [
			{
				"id": 1,
				"description": "Wood",
				"quantity": 50,
				"price": "$10"
			}
		]
	},
	{
		"id": 2,
		"date": "2024-03-24",
		"message": "Order testing",
		"status": "In transit",
		"user": {
			"email": "shopstaff@email.com"
		},
		"items": [
			{
				"id": 2,
				"description": "Iron",
				"quantity": 150,
				"price": "$20"
			}
		]
	},
	{
		"id": 3,
		"date": "2024-03-24",
		"message": "Order testing",
		"status": "Delivered",
		"user": {
			"email": "shopadmin@email.com"
		},
		"items": [
			{
				"id": 3,
				"description": "Plastic",
				"quantity": 500,
				"price": "$5"
			}
		]
	}
] 
```

GET/orders/<order_id> 
example /orders/1 will return order with id 1
```
{
	"id": 1,
	"date": "2024-03-24",
	"message": "Order testing",
	"status": "Processing",
	"user": {
		"email": "shopadmin@email.com"
	},
	"items": [
		{
			"id": 1,
			"description": "Wood",
			"quantity": 50,
			"price": "$10"
		}
	]
}
```
POST/order
Creates new order with objects in json
```
{
	"message": "updated",
	"status": "processing"
}
```
The above will be added to make a new order
```
{
	"id": 4,
	"date": "2024-03-24",
	"message": "updated",
	"status": "processing",
	"user": {
		"email": "shopadmin@email.com"
	},
	"items": []
}
```
PUT, PATCH/order/<order_id>
```
{
	"message": "status update",
	"status": "delayed"
}
```
above will be applied to update the record on order id 4
```
{
	"id": 4,
	"date": "2024-03-24",
	"message": "updated",
	"status": "processing",
	"user": {
		"email": "shopadmin@email.com"
	},
	"items": []
}
```
DELETE/order/<order_id>
delete order with id 4
```
{
	"message": "Order 4 has been deleted"
}
```
_______________
Item controller

POST/<order_id>/items
POST/1/items
add items to order id 1
```
	{
		"id": 1,
		"date": "2024-03-24",
		"message": "Order testing",
		"status": "Processing",
		"user": {
			"email": "shopadmin@email.com"
		},
		"items": [
			{
				"id": 1,
				"description": "Wood",
				"quantity": 50,
				"price": "$10"
			}
		]
	}
```
Create order with the new fields below
```
{
	"description": "steel",
	"quantity": "20",
	"price": "$50"
}
```
After creating item order, the id will now have 2 item orders with id 1 and 4
```
{
	"id": 1,
	"date": "2024-03-24",
	"message": "Order testing",
	"status": "Processing",
	"user": {
		"email": "shopadmin@email.com"
	},
	"items": [
		{
			"id": 1,
			"description": "Wood",
			"quantity": 50,
			"price": "$10"
		},
		{
			"id": 4,
			"description": "steel",
			"quantity": 20,
			"price": "$50"
		}
	]
}
```
PUT,PATCH/<order_id>/items/<items_id>
order/1/items/1
update existing items in order with item id 1 with
```
{
	"description": "copper",
	"quantity": "100",
	"price": "$500"
}
```
updated item id 1 now changed with fields specified above 
```
{
	"id": 1,
	"date": "2024-03-24",
	"message": "Order testing",
	"status": "Processing",
	"user": {
		"email": "shopadmin@email.com"
	},
	"items": [
		{
			"id": 4,
			"description": "steel",
			"quantity": 20,
			"price": "$50"
		},
		{
			"id": 1,
			"description": "copper",
			"quantity": 100,
			"price": "$500"
		}
	]
}
```
DELETE/<order_id>/items/<items_id>
order/1/items/1
```
{
	"message": "Item with id 1 has been deleted"
}
```
item id 1 now deleted from object
```
{
	"id": 1,
	"date": "2024-03-24",
	"message": "Order testing",
	"status": "Processing",
	"user": {
		"email": "shopadmin@email.com"
	},
	"items": [
		{
			"id": 4,
			"description": "steel",
			"quantity": 20,
			"price": "$50"
		}
	]
}
```
_______________
auth_controller

POST/auth/register
create new email and password
```
{
	"email": "new_member@email.com",
	"password": "abcdefg"
}
```
will return 
```
{
	"id": 3,
	"email": "new_member@email.com",
	"is_admin": false
}
```

POST/auth/login
will create a jwt token for authentication
```
{
	"email": "new_member@email.com",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTI4NDQyNSwianRpIjoiNzg4NDQ1ODQtZWE0Mi00Mjc0LThlZmYtZmU0YTcxNzEwMzBjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE3MTEyODQ0MjUsImNzcmYiOiJjZjdjMzdjOC1mNzVjLTQ3YzQtYmFkMC0wOWM5NTgxYjZhOWEiLCJleHAiOjE3MTEzNzA4MjV9.2FDJSrUcNQa0dPwpZkM93XHqh7lUiGOM0JYMB3Agc9s",
	"is_admin": false
}
```

___________________________________________
R6. An ERD for your app

![image](https://github.com/navko11/flaskapi/assets/127573434/b3c4fc9c-f1e5-450f-b184-6c68c216beec)


___________________________________________
R7. Detail any third party services that your app will use

The third party services used are imported as libraries in the code found in requirements.txt 
some of the main services are listed to be:

Flask - A web framework for building web applications in python
SQLAlchemy - An SQL toolkit and ORM library for python constructs
Marshmallow - Serialize and deserializes objects and converts them into python objects 
Bcrypt - Secures passwords by hashing them for increased security

Insomnia - An API client used for testing http requests (GET, POST, PUT, PATCH, DELETE)

___________________________________________
R8. Describe your projects models in terms of the relationships they have with each other

My project is the simplest form of the idea which only has 3 models:

Users - The users model is the start of the ERD and holds a one to many relationship with the orders model, where one user can have many orders. 
Orders - The order model holds a one to many relationship with the items model, where one order can have many items.
Items - The items model is at the and of the ERD and as such holds the "many" relation to the "one" relation of orders.

___________________________________________
R9. Discuss the database relations to be implemented in your application 

___________________________________________
R10. Describe the way tasks are allocated and tracked in your project

Tasks are created and then recorded depending on the request given (GET, POST, PUT/PATCH, DELETE).

GET - Will collect all the seeded data and any additional instances created.  
POST - Creates a new instance in the route where the fields are set and requested. The number of POST requests can be tracked by the enumeration of id's being created
PUT/PATCH - Updates any existing fields if necessary ex. status update from "in transit" to "delivered"
DELETE - Deletes an instance for redundance purposes.




