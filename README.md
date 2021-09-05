# DevMuscles-Server

## Routes
# DevMuscles-Server

## Routes

|Option|Route|Allowable Methods|
|---|---|---|
|1|/users|GET, POST|
|2|/users/id|GET, PUT, DELETE|
|3|/workouts|GET, POST|
|4|/workouts/id|GET, PUT, DELETE|
- Option 1 - GET --> gets all users from the DB, expected outcome:
```
[
    {
        "id": 1,
        "username": "admin",
        "first_name": "admin",
        "last_name": "admin"
    },
    {
        "id": 12,
        "username": "Akash",
        "first_name": "Akash",
        "last_name": "surname"
    },
    ...etc
]
```
- Option 1 - POST --> adds a user to the database, the request body needs to be in format following format:
```
{
    "username": "example",
    "first_name": "example",
    "last_name": "example",
    "password": "test123.",
    "password_confirmation": "test123."
}
```

- Option 2 - GET --> will get one particular user given an id, e.g. ```/users/12``` will yeild:
```
{
    "id": 12,
    "username": "Akash",
    "first_name": "Akash",
    "last_name": "surname"
}
```
- Option 2 - PUT --> can update details of one particular user given an id, the request body needs to be in the format below. e.g to change the last name of the user Akash:

```
send this:
{
    "id": 12,
    "username": "Akash",
    "first_name": "Akash",
    "last_name": "Khambay"
}
```
- Option 2 - DELETE --> ```/users/12``` with a request method of delete will remove Akash from the database.
- Option 3 - GET --> gets all workouts that exist in the DB, expected outcome (Note - matched with the users table by user_id using a foreign key):
```
[
    {
        "id": "1",
        "name": "calves",
        "user_id": 12
    },
    {
        "id": "2",
        "name": "back",
        "user_id": 24
    },
    ...etc
]
```
- Option 3 - POST --> adds a new workout to the DB, the request body needs to be in format following format (Note: id will need to be given as a str atm, will change later to incoporate uuid, also the corresponding user_id needs to be given to match a workout with a user):
```
{
    "id": "3",
    "name": "shoulders",
    "user_id": 24
}
```
- Option 4 - GET --> will get one particular workout given an id, e.g. ```/workouts/1``` will yeild:
```
{
    "id": "1",
    "name": "calves",
    "user_id": 12
}
```
- Option 4 - PUT --> can update details of one particular workout given an id, the request body needs to be in the format below. e.g to change the workout name in the example above from calves to chest:

```
send this:
{
    "id": "1",
    "name": "chest",
    "user_id": 12
}
```
- Option 4 - DELETE --> ```/workouts/1``` with a request method of delete will remove the chest workout from the database.
