# DevMuscles-Server

## Routes
# DevMuscles-Server
https://devmuscles.herokuapp.com/
## Routes

|Route|Allowable Methods|
|---|---|
|/login|POST|
|/users|GET, POST|
|/users/:user_id|GET, PUT, DELETE|
|/users/:user_id/workouts|GET, POST|
|/users/:user_id/workouts/:workout_id|GET, PUT, DELETE|
|/users/:user_id/workouts/:workout_id/exercises|GET, POST|
|/users/:user_id/workouts/:workout_id/exercises/:exercise_id|GET, PUT, DELETE|
|/users/:user_id/dates|GET, POST|
|/users/:user_id/dates/:date_id|GET, PUT, DELETE|

- ```/users``` --> GET --> gets all users from the DB, expected outcome:
```
[
  {
    "id": 91,
    "username": "Testuser",
    "email": "test@example.com"
  },
  {
    "id": 92,
    "username": "test",
    "email": "test@example.com"
  },
  ...etc
]
```
- ```/users``` - POST --> in order to sign in, you will need to create a new user, let's create a user for Jawwad, send data in the following format:
```
{
    "username": "Jawwad",
    "email": "jawwad@example.com",
    "password": "password",
    "password_confirmation": "password"
}

The server will respond with a username, token and generated id, for example, for the user we just created:

{
  "username": "Jawwad",
  "token": "6dfed80bd9468f955f647b0ff4fe52b5e23360db",
  "id": 94
}

NOTE: IT IS IMPORTANT TO STORE THE TOKEN AS WELL AS ID ON THE FRONT END, YOU WILL NOT BE AUTHORISED TO ACCESS ANY OF THE REMAINING ROUTES WITHOUT THEM.

However, if the username you have selected already exists, the server will respond with:

{
  "username": [
    "A user with that username already exists."
  ]
}
```

- ```/login``` - POST --> if you already have an account, you can login. For example, let's login for Jawwad:
```
{
    "username": "Jawwad",
    "password": "password"
}

The server will respond with the corresponding token for that user and their id.

{
  "token": "6dfed80bd9468f955f647b0ff4fe52b5e23360db",
  "id": 94
}

Once again, note: save token and id on the front end. If the credientials are wrong, you will receive the following:

{
  "non_field_errors": [
    "Unable to log in with provided credentials."
  ]
}
```

- ```/users/:user_id``` --> GET --> gets the particular user from the DB, routes have been protected, you will not be able to access any other id except your own, hence why its important to store your id and token when you receive them after signing up or logging in, expected outcome for Jawwad: ```/users/94```:
```
{
  "id": 94,
  "username": "Jawwad",
  "email": "jawwad@example.com"
}

Will not be able to access this without token in the request Header, will receive the following error:

{
  "detail": "Authentication credentials were not provided."
}

If you try accessing a different user id e.g. ```/users/12```, you will receive:

"You are unauthorized to access this"
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
