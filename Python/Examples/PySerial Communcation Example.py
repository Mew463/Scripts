import serial 
import time 

def setup(serial_name, baud_rate):
    ser = serial.Serial(serial_name, baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()

def send_message(ser, message):
   if(message[-1] != '\n'):
       message = message + '\n'
   ser.write(message.encode('utf-8'))

   
#Receive a message from Serial and limit it to num_bytes (default of 50)
def receive_message(ser, num_bytes=50):
    if(ser.in_waiting > 0):
        return ser.readline(num_bytes).decode('utf-8')
    else:
        return None

def main():
    ser = setup("COM9", 115200)
    time.sleep(2) #pretty important, wait for mcu to intiailize first
    send_message(ser, "hello world\n")
    time.sleep(3)
    message = receive_message(ser)
    print(message)
    close(ser)

"""
Main entrypoint for the application
"""
if __name__== "__main__":
   main()