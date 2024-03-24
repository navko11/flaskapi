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




