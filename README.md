# DevMuscles-Server

## Routes

|Option|Route|Allowable Methods|
|---|---|---|
|1|/users|GET, POST|
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
        "first_name": "akash",
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
