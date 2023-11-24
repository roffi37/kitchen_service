
# Kitchen Service

Imagine you are the owner of restaurant, and you want to improve the communication & rules between your cooks on the kitchen. For this purpose you want to build management system, in which Cooks can create new Dishes & Dishtypes, and also specify, Cooks which are responsible for every Dishes cooking.


## Demo

https://kitchen-service-9rkb.onrender.com/

# Functionality
On this service, you can use the following functions: read dish types, read dishes, read cooks; register a user (cooks); create dish types, update, delete; create dishes, delete, update; Offcourse if you are a cook :)


## Environment Variables


To deploy this project run

```bash
  python -m venv venv
  source venv/scripts/activate
  python manage.py migrate
  python manage.py loaddata db.json
  python manage.py runserver
```

![image](https://github.com/roffi37/kitchen_service/assets/143605204/9482d375-0075-4a9e-a900-086d76dd6199)
