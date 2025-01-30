from pynput.keyboard import Key, Listener, KeyCode, Controller
import time
key_state = {}

# Function to be called when a key is pressed
def on_press(key):        
    key = str(key).strip("'")
    if len(key) == 1 and key.isupper():
        key = key.lower()
    key_state[key] = True  # Update key state to pressed

# Function to be called when a key is released
def on_release(key):
    key = str(key).strip("'")
    if len(key) == 1 and key.isupper():
        key = key.lower()
    key_state[key] = False  # Update key state to released
    
def get_key_state(key):
    # print(key_state)
    if (key in key_state and key_state[key]):
        return True
    else:
        return False
    

keyboard = Controller()
def pushWeaponButton():
    keyboard.press('l')
    time.sleep(.02)
    keyboard.release('l')
    time.sleep(.02)