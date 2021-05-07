import serial, sys, os

flag = 1

arduino = serial.Serial('/dev/ttyACM0', 9600)

dataSend = sys.argv[1]

path = '/home/user/Desktop/'
filename = '/Report.pdf'

while True:
	readData = arduino.readline()
	print(readData)
	if(flag):
		arduino.write(dataSend)
		flag = 0
	if "PATIENT" in readData:
		id = readData[7:len(readData)-2];
		os.system('xdg-open ' + path + id + filename)
