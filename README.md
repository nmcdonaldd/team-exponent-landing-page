# Team Exponent

## FeatherPad
Link to webpage can be found [here](https://featherpad.herokuapp.com/).

## FeatherPad API Endpoints

+ [/api/subscribers](https://github.com/nmcdonaldd/team-exponent-landing-page#apisubscribers)
+ [/api/temp_hum](https://github.com/nmcdonaldd/team-exponent-landing-page#apitemp_hum)
+ [/api/temp_hum/create](https://github.com/nmcdonaldd/team-exponent-landing-page#apitemp_humcreate)
+ [/api/temp_hum/update/<_id_>](https://github.com/nmcdonaldd/team-exponent-landing-page#apitemp_humupdateid)
+ [/api/temp_hum/delete/<_id_>](https://github.com/nmcdonaldd/team-exponent-landing-page#apitemp_humdeleteid)

#
### /api/subscribers
Returns a collection of users in JSON format that have subscribed to our website to learn more.

### Example Request
*GET https://featherpad.herokuapp.com/api/subscribers*

### Example Response
```json
[
  {
    "email": "lkasjf@gmail",
    "first_name": "Nick",
    "id": 2
  },
  {
    "email": "poop@gmail.com",
    "first_name": "Nick",
    "id": 12
  },
  {
    "email": "poop@galskdjfl",
    "first_name": "Nick",
    "id": 22
  },
  {
    "email": "2j@gmail.com",
    "first_name": "Klasdjflk",
    "id": 32
  },
  {
    "email": "rickghome@gmail.com",
    "first_name": "Rick Gessner",
    "id": 42
  },
  {
    "email": "jharms@gmail.com",
    "first_name": "Jack",
    "id": 52
  },
  {
    "email": "123@gmail.com",
    "first_name": "Sam",
    "id": 62
  },
  {
    "email": "magoopoop@gmail.com",
    "first_name": "Poop-magoo",
    "id": 72
  },
  {
    "email": "lala@gmail.com",
    "first_name": "Vicky",
    "id": 82
  }
]
```

#
### /api/temp_hum
Returns a collection of temperature and humidity readings taken from our prototype FeatherPad unit in JSON format. Temperature is given in degrees Celsius and humidity is given as a percentage.

### Example Request
*GET https://featherpad.herokuapp.com/api/temp_hum*

### Example Response
```json
[
  {
    "humidity": 49,
    "id": 122,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:13:49 GMT"
  },
  {
    "humidity": 49,
    "id": 132,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:14:50 GMT"
  },
  {
    "humidity": 49,
    "id": 142,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:15:52 GMT"
  },
  {
    "humidity": 48,
    "id": 152,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:24:10 GMT"
  },
  {
    "humidity": 47,
    "id": 162,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:25:12 GMT"
  },
  {
    "humidity": 48,
    "id": 172,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:26:21 GMT"
  },
  {
    "humidity": 48,
    "id": 182,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:27:25 GMT"
  },
  {
    "humidity": 48,
    "id": 192,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:28:29 GMT"
  },
  {
    "humidity": 48,
    "id": 202,
    "temperature": 21,
    "timestamp": "Sun, 07 May 2017 23:29:33 GMT"
  },
  {
    "humidity": 48,
    "id": 212,
    "temperature": 20,
    "timestamp": "Sun, 07 May 2017 23:30:35 GMT"
  }
]
```

#
### /api/temp_hum/create
Adds a new *temp_hum reading* data set with the provided temperature and humidity. Note, a set of temperature and humidity data must be passed with the request. Upon success, the request will return a _temp_hum_ reading with new values.

### Example Request
*POST https://featherpad.herokuapp.com/api/temp_hum/create*
```json
{
  "temperature": 32,
  "humidity": 51
}
```

### Example Response
```json
{
  "humidity": 51,
  "id": 122,
  "temperature": 32,
  "timestamp": "Sun, 07 May 2017 23:13:49 GMT"
}
```

#
### /api/temp_hum/update/<_id_>
Updates the *temp_hum reading* data set with identifier _id_. Note, a set of temperature and humidity data must be passed with the request. Upon success, the request will return a _temp_hum_ reading with updated values.

### Example Request
*PUT https://featherpad.herokuapp.com/api/temp_hum/update/122*
```json
{
  "temperature": 43,
  "humidity": 62
}
```

### Example Response
```json
{
  "humidity": 62,
  "id": 122,
  "temperature": 43,
  "timestamp": "Sun, 07 May 2017 23:13:49 GMT"
}
```

#
### /api/temp_hum/delete/<_id_>
Deletes the *temp_hum reading* data set with identifier _id_. Upon success, the request will return a _temp_hum_ reading with deleted values

### Example Request
*DELETE https://featherpad.herokuapp.com/api/temp_hum/update/122*

### Example Response
```json
{
  "humidity": 62,
  "id": 122,
  "temperature": 43,
  "timestamp": "Sun, 07 May 2017 23:13:49 GMT"
}
```
