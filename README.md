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

- ```/users/:user_id``` --> DELETE --> will remove the user from the database, user will lose all their info.
 
- ```/users/:user_id/workouts``` --> GET --> gets all workouts for that user from the DB, expected outcome for Jawwad ```/users/94/workouts```(have added 2 workouts before):
```
[
  {
    "id": "2b9208a8-8543-4444-a858-5dacfe361c30",
    "name": "chest",
    "user_id": 94
  },
  {
    "id": "cceb797e-e4ff-404b-aa65-abd3ed6c6db3",
    "name": "back",
    "user_id": 94
  }
]
```

- ```/users/:user_id/workouts``` --> POST --> This would post a new workout for that user, expected to receive data in the following format:
```
{
    "name": "shoulders"
}

This would add another workout named shohulders to the user Jawwad. The server will respond in the following format:

{
  "id": "edb39584-c476-491e-827e-6e4806df00ad",
  "name": "shoulders",
  "user_id": 94
}
```

- ```/users/:user_id/workouts/:workout_id``` --> GET --> gets one particular workout for a user. E.g to get Jawwad's shoulder workout, ```/users/94/workouts/edb39584-c476-491e-827e-6e4806df00ad```:
```
{
  "id": "edb39584-c476-491e-827e-6e4806df00ad",
  "name": "shoulders",
  "user_id": 94
}
```

- ```/users/:user_id/workouts/:workout_id``` --> PUT --> To update the name of a particular workout. E.g to change Jawwad's 'shoulder' workout, to 'intense shoulder' ```/users/94/workouts/edb39584-c476-491e-827e-6e4806df00ad```
```
send this:
{
    "name": "intense shoulders"
}
```

- ```/users/:user_id/workouts/:workout_id``` --> DELETE --> would delete the workout corresponding to the given id for the user.
```
Response upon successful deletion: "Workout has successfully been deleted"
```

- ```/users/:user_id/workouts/:workout_id/exercises``` --> GET --> gets all exercises associated with that user and that workout. E.g. to see all exercises in Jawwad's chest workout, ```/users/94/workouts/2b9208a8-8543-4444-a858-5dacfe361c30/exercises```, (note: previously populated with 2 exercises):
```
[
  {
    "id": "4cf91436-df29-4e4c-a7c3-a0df3f0f833c",
    "name": "bench press",
    "reps": 6,
    "weight": "75.0",
    "workout_id": "2b9208a8-8543-4444-a858-5dacfe361c30"
  },
  {
    "id": "1c15e784-3a61-4a44-b35e-0684b457d699",
    "name": "push ups",
    "reps": 100,
    "weight": "60.0",
    "workout_id": "2b9208a8-8543-4444-a858-5dacfe361c30"
  }
]
```

- ```/users/:user_id/workouts/:workout_id/exercises``` --> POST --> will add a new exercise to that workout. E.g to add another chest exercise for Jawwad, you will need to send data in the following format to ```/users/94/workouts/2b9208a8-8543-4444-a858-5dacfe361c30/exercises```:
```
{
    "name": "dips",
    "reps": 40,
    "weight": 60.0
}

Server wil respond with:

{
  "id": "612a686a-9175-468a-a1d7-b6d422325e86",
  "name": "dips",
  "reps": 40,
  "weight": "60.0",
  "workout_id": "2b9208a8-8543-4444-a858-5dacfe361c30"
}
```

- ```/users/:user_id/workouts/:workout_id/exercises/:exercise_id``` --> GET --> will get the corresponding exercise for a given workout and user. E.g. to get Jawwad's push ups exercise, ```/users/94/workouts/2b9208a8-8543-4444-a858-5dacfe361c30/exercises/1c15e784-3a61-4a44-b35e-0684b457d699```:
```
{
  "id": "1c15e784-3a61-4a44-b35e-0684b457d699",
  "name": "push ups",
  "reps": 100,
  "weight": "60.0",
  "workout_id": "2b9208a8-8543-4444-a858-5dacfe361c30"
}
```

- ```/users/:user_id/workouts/:workout_id/exercises/:exercise_id``` --> PUT --> let's update the number of reps for Jawwad's push up exercise, send:
```
{
    "name": "push ups",
    "reps": 120,
    "weight": 60.0
}
```

- ```/users/:user_id/workouts/:workout_id/exercises/:exercise_id``` --> DELETE --> will delete that particular exercise from the workout.
```
Response upon successful deletion: "Exercise has successfully been deleted"
```

- ```/users/:user_id/dates``` --> GET --> gets all dates that have a workout has been scheduled on, e.g. ```/users/94/dates``` will respond with the following, (note: previously scheduled a chest workout):
```
[
  {
    "id": "55b1fa9a-89c4-4ff0-8e4e-b32ee582f7bd",
    "date": "2021-09-08",
    "time": 1630,
    "completed": false,
    "workout_id": "2b9208a8-8543-4444-a858-5dacfe361c30",
    "user_id": 94
  }
]
```

- ```/users/:user_id/dates?date=yyyy-mm-dd``` --> GET --> if you add a query parameter of date in the correct format, you will receive a filtered list of dates where the dates match the query param.


- ```/users/:user_id/dates``` --> POST --> you can schedule a workout on a particular day. E.g. for Jawwad, lets schdedule his back workout for the 10th September 2021 at 1.45pm.
```
Send this:
{
    "workout_id": "cceb797e-e4ff-404b-aa65-abd3ed6c6db3",
    "date": "2021-09-10",
    "time": "1345",
    "completed": "False"
}

Server will respond with:
{
  "id": "f5c76c08-c936-44cb-8ef7-72a8ef402013",
  "date": "2021-09-10",
  "time": 1345,
  "completed": false,
  "workout_id": "cceb797e-e4ff-404b-aa65-abd3ed6c6db3",
  "user_id": 94
}

Note: You will need to provide the workout_id of the corresponding workout you wish to schedule. Also note that the date field is in the format "yyyy-mm-dd"
```

- ```/users/:user_id/dates/:date_id``` --> GET --> will get the corresponding date, additionally it will also send back details of the workout associated with that date, E.g. ```/users/94/dates/f5c76c08-c936-44cb-8ef7-72a8ef402013```:
```
{
  "date": {
    "id": "f5c76c08-c936-44cb-8ef7-72a8ef402013",
    "date": "2021-09-10",
    "time": 1345,
    "completed": false,
    "workout_id": "cceb797e-e4ff-404b-aa65-abd3ed6c6db3",
    "user_id": 94
  },
  "workout": {
    "id": "cceb797e-e4ff-404b-aa65-abd3ed6c6db3",
    "name": "back",
    "user_id": 94
  }
}
```

- ```/users/:user_id/dates/:date_id``` --> PUT --> E.g. let's update the time of the back workout and schedule it to 5pm for Jawwad, you will need to send the following to ```/users/94/dates/f5c76c08-c936-44cb-8ef7-72a8ef402013```:
```
{
    "workout_id": "cceb797e-e4ff-404b-aa65-abd3ed6c6db3",
    "date": "2021-09-10",
    "time": "1700",
    "completed": "False"
}
```

```/users/:user_id/dates/:date_id``` --> DELETE --> will delete a scheduled date.
```
Response upon successful deletion: "Date has successfully been deleted"
```
