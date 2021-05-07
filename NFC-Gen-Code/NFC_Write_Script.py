import serial, sys

flag = 1

arduino = serial.Serial('/dev/ttyACM0', 9600)

dataSend = sys.argv[1]

while True:
	print(arduino.readline())
	if(flag):
		arduino.write(dataSend)
		flag = 0	
	if(arduino.readline() == "Done!\r\n"):
		sys.exit(1)