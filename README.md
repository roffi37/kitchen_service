# kitchen_service
Imagine you are the owner of restaurant, and you want to improve the communication & rules between your cooks on the kitchen. For this purpose you want to build management system, in which Cooks can create new Dishes & Dishtypes, and also specify, Cooks which are responsible for every Dishes cooking.

Credentials:
`login`: **user.admin**
`password`: **y390SBr7**
=====================
1. python -m venv venv
2. source venv/scripts/activate
3. run python manage.py migrate
4. run python manage.py loaddata db.json
5. run python manage.py runserver
-----------------------------------
On this service, you can use the following functions: read dish types, read dishes, read cooks; register a user (cooks); create dish types, update, delete; create dishes, delete, update;
