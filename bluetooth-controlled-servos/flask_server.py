from flask import Flask
from flask import request
import json
import bluetooth

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recieve_webhook():
	print (request.form['Body'])
	if request.form['Body'] == 'lamp-on':
		print ('Turn light on')
		bluetooth.BluetoothSerialPortController.move_servo_two()
	elif request.form['Body'] == 'lamp-off':
		print ('Turn light off')
		bluetooth.BluetoothSerialPortController.move_servo_one()
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=3000)