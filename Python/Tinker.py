# Importing Libraries
import serial
arduino = serial.Serial(port='COM20', baudrate=115200, timeout=.1)

arduino.write(bytes("a", 'utf-8'))


