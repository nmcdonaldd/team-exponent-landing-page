# Team Exponent

## FeatherPad
Link to webpage can be found [here](https://featherpad.herokuapp.com/).

## FeatherPad API Endpoints
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
