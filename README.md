# bikesaledemo
A Flask API Bicycle sales API demo code

# Intro

Learning about Flask and creating nice REST API's

# Reasoning

I like bikes, and I like Python.

# Install
_I wrote it for Python 3.5, but it may work in Python 2.7 YMMV_

- `git clone https://github.com/ephergent/bikesaledemo.git`
- `cd bikesaledemo`
- `pip install requirements.txt`
- `python app.py`

Open `http://127.0.0.1:5000/` in browser of choice. 

_note: it will be empty on start up_

# API Resources:

### GET a bike and/or bikes
- To return all bikes in memory:
	`curl -X GET http://127.0.0.1:5000/`
- To return a specific bike id (i.e. bike1)
	`curl -X GET http://127.0.0.1:5000/bike1`

### POST a bike
_Requires: bicycle, year, color, size, and price_

`curl -X POST http://127.0.0.1:5000/bike1 -H 'content-type: application/json' -d '{"bicycle": "Trek 930","year": "1995","color": "blue/green","size": "21 inches","price": 549.99}'`

### PUT update a bike, also create if none exist
_Requires: bicycle, year, color, size, and price_

`curl -X PUT http://127.0.0.1:5000/bike1 -H 'content-type: application/json' -d '{"bicycle": "Trek 930","year": "1995","color": "blue/green","size": "21 inches","price": 249.99}'`

### DELETE a bike
`curl -X DELETE http://127.0.0.1:5000/bike1`

# Conclusion

This is just a demo to practice Flask and Flask-restful
