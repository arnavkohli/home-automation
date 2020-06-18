from serial import Serial

class BluetoothSerialPortController:
	ser = Serial('/dev/tty.HC-05-SerialPort')

	@classmethod
	def move_servo_one(cls):
		cls.ser.write(b'\x01')

	@classmethod
	def move_servo_two(cls):
		cls.ser.write(b'\x02')