''' =========================================================================================== '''
# Our Chat RESTful App

''' =========================================================================================== '''
# third-party imports
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import jsonify
from flask import abort
from flask import url_for   #what

# local imports
from app import create_app
from app import models
from app import db
from env import FLASK_CONFIG

# pythong libraries
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

''' =========================================================================================== '''
# instantiate the app
app = create_app(FLASK_CONFIG)

''' =========================================================================================== '''
# define our routes

HUMIDITY_JSON_KEY_IDENTIFIER = 'humidity'
TEMPERATURE_JSON_KEY_IDENTIFIER = 'temperature'

''' If user tries to access undefined page, post 404 error'''
@app.errorhandler(404)
def page_not_found(e):
	return render_template('home/404.html'), 404

'''
Description: Render the main chat view here from templates
Input: None
Return Type: HTML, a view generated by render_template()
'''
@app.route('/')
def chat_view():
	new_visitor = models.Visitor()
	db.session.add(new_visitor)
	db.session.commit()
	return render_template('home/index.html', title='Home')


@app.route('/api/login_mobile/create/<string:username>/<string:password>', methods=['POST'])
def mobile_login(username, password):
	# Should do some sort of checking to make sure that the username and password works.
	# TODO: FIX THE FOLLOWING.
	devices = models.Device.query.all()	# This should be the 1234 device.
	toReturn = []
	for device in devices:
		toReturn.append(device.toDict())
	return jsonify(toReturn)

@app.route("/login", methods=['POST'])
def logging_in():
	the_username = request.form['username']
	the_password = request.form['password']

	user = models.User.query.filter_by(username = the_username).first()
	if user is not None and the_password == user.password:
		session['the_user'] = user
		return render_template('home/profile.html', username = the_username)
	return redirect('/')

@app.route("/create_account", methods=['POST'])
def creating_account():
	return render_template('home/create.html')

@app.route('/submit', methods=['POST'])
def subscribing():
	the_subscriber_fname = request.form['name']
	the_subscriber_email = request.form['email_address']

	# Making it so that the name appears with a capital first letter
	the_subscriber_fname = ' '.join(word[0].upper() + word[1:] for word in the_subscriber_fname.lower().split())

	new_db_subscriber = models.Subscriber(first_name=the_subscriber_fname, email=the_subscriber_email)
	print("new subscriber: ", new_db_subscriber.first_name, new_db_subscriber.email)

	db.session.add(new_db_subscriber)
	db.session.commit()

	return render_template('home/thankyou.html', title='Thank You!', first_name=the_subscriber_fname)

@app.route('/stats')
def statistics():
	#Gotta figure out how to get the last visitor to visit landing page

	recent_visitor = models.Visitor.query.order_by(models.Visitor.id.desc()).first()
	recent_visit_time = recent_visitor.time
	all_visits = models.Visitor.query.count()

	recent_subscriber = models.Subscriber.query.order_by(models.Subscriber.id.desc()).first()
	recent_subscribe_name = recent_subscriber.first_name
	all_signups = models.Subscriber.query.count()
	return render_template('home/stats.html', title='Stats', last_visit = recent_visit_time  , last_signup = recent_subscribe_name, total_visits = all_visits , total_signups = all_signups)

@app.route("/api/subscribers")
def subscribers():
	allSubs = models.Subscriber.query.all()
	jsonToReturn = []
	for subscriber in allSubs:
		jsonToReturn.append({'id': subscriber.id, 'first_name': subscriber.first_name, 'email': subscriber.email})
	return jsonify(jsonToReturn)

@app.route("/api/temp_hum/<string:device_id>")
def temp_hums(device_id):
	# Grab devicePrimaryKey given the mac_address
	devicePrimaryKey = get_device_primary_key(device_id)
	if devicePrimaryKey is None:
		return abort(404)
	# Now, grab all temp_hum objects that have the device_id = devicePrimaryKey
	all_temp_hum = models.temp_hum.query.filter_by(device_id=devicePrimaryKey)
	jsonToReturn = []
	for value in all_temp_hum:
		jsonToReturn.append(value.toDict())
	return jsonify(jsonToReturn)

@app.route("/api/temp_hum/create/<string:device_id>", methods=["POST"])
def create_temp_hum_reading(device_id):
	if not request.json:
		return abort(400)
	values = request.get_json()
	temp = values[TEMPERATURE_JSON_KEY_IDENTIFIER]
	hum = values[HUMIDITY_JSON_KEY_IDENTIFIER]
	devicePrimaryKey = get_device_primary_key(device_id)
	# TODO: Check to make sure the device_id is valid?
	new_reading = models.temp_hum(temperature=temp, humidity=hum, device_id=devicePrimaryKey)
	db.session.add(new_reading)
	db.session.commit()

	return jsonify(new_reading.toDict()), 201

@app.route("/api/temp_hum/update/<string:device_id>/<int:entry_id>", methods=["PUT"])
def update_temp_hum_reading(device_id, entry_id):
	if not request.json:
		return abort(400)

	new_values = request.get_json()
	updated_reading = models.temp_hum.query.get(entry_id)
	devicePrimaryKey = get_device_primary_key(device_id)

	# If the primary key does not exist, we cannot update any values for it!
	if devicePrimaryKey is None:
		return abort(404)

	# Ensure that the device_id that is being given matches the id of the device
	#  of the temp_hum reading requesting to be updated.
	if updated_reading.id != devicePrimaryKey:
		return abort(403)

	if updated_reading is None:
		return abort(400)

	updated_reading.temperature = new_values[TEMPERATURE_JSON_KEY_IDENTIFIER]
	updated_reading.humidity = new_values[HUMIDITY_JSON_KEY_IDENTIFIER]

	db.session.commit()

	return jsonify(updated_reading.toDict()), 201

@app.route("/api/device/create/<string:device_id>", methods=["POST"])
def newDevice(device_id):
	devicePrimaryKey = get_device_primary_key(device_id)

	# If the device id is already in use, we cannot create it again!
	if devicePrimaryKey is not None:
		return abort(403)

	device = models.Device(macAddress=device_id)
	db.session.add(device)
	db.session.commit()

	return jsonify(device.toDict())

@app.route("/api/device/delete/<string:device_id>", methods=["DELETE"])
def deleteDevice(device_id):
	devicePrimaryKey = get_device_primary_key(device_id)
	if devicePrimaryKey is None:
		return abort(403)

	device_to_delete = models.Device.query.filter_by(mac_address=device_id).first()
	db.session.delete(device_to_delete)
	db.session.commit()
	# TODO: Remove all readings! (i.e. temp_hum, light_sensor, force_reading)
	'''
	for reading in all_readings:
		db.session.delete(reading)

	db.session.commit()
	'''
	return jsonify(device_to_delete.toDict())

@app.route("/api/temp_hum/delete/<string:device_id>/<int:entry_id>", methods=["DELETE"])
def delete_temp_hum_reading(device_id, entry_id):
	to_delete = models.temp_hum.query.get(entry_id)
	devicePrimaryKey = get_device_primary_key(device_id)

	# If the primary key does not exist, we cannot update any values for it!
	if devicePrimaryKey is None:
		return abort(404)

	# Ensure that the device_id that is being given matches the id of the device
	#  of the temp_hum reading requesting to be updated.
	if to_delete.id != devicePrimaryKey:
		return abort(403)

	if to_delete is None:
		return abort(400)

	db.session.delete(to_delete)
	db.session.commit()

	return jsonify(to_delete.toDict()), 201

@app.route("/display_data/<int:device_id>")
def get_data(device_id):
	all_forces = models.force_reading.query.all()
	all_temp_hum = models.temp_hum.query.all()

	print(all_temp_hum)
	return render_template("home/api_data.html", forces = all_forces, temps_hums = all_temp_hum)

def get_device_primary_key(device_id):
	# First, grab the device primary_key associated with the device_id(mac_address) given
	devicePrimaryKey = models.Device.query.filter_by(mac_address=device_id).first()
	if devicePrimaryKey is None:
		return None
	else:
		return devicePrimaryKey.id

''' =========================================================================================== '''
# run the app
if __name__ == '__main__':
    app.run()
