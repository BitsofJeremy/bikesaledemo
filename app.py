from flask import Flask,request,render_template
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

bikes = {}

def abort_if_bike_doesnt_exist(bikeid):
	if bikeid not in bikes:
		abort(404, message="Bike {0} doesn't exist.".format(bikeid))


# Setup args for data imput
parser = reqparse.RequestParser()
parser.add_argument('bicycle', type=str, help='Enter Bicycle name')
parser.add_argument('year', type=str, help='Enter Bicycle year')
parser.add_argument('color', type=str, help='Enter Bicycle color')
parser.add_argument('size', type=str, help='Enter Bicycle size')
parser.add_argument('price', type=float, help='Enter Bicycle price')

class Bike(Resource):

	def get(self, bikeid):
		abort_if_bike_doesnt_exist(bikeid)
		return {bikeid: bikes[bikeid]}

	def post(self, bikeid):
		args = parser.parse_args()
		bikes[bikeid] = args
		return args, 201

	def put(self, bikeid):
		args = parser.parse_args()
		bikes[bikeid] = args
		return args, 201 

	def delete(self, bikeid):
		abort_if_bike_doesnt_exist(bikeid)
		del bikes[bikeid]
		return {bikeid: 'deleted'}

class Bikes(Resource):
	def get(self):
		return bikes


api.add_resource(Bike, '/api/<string:bikeid>')
api.add_resource(Bikes, '/api/')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host="0.0.0.0")
