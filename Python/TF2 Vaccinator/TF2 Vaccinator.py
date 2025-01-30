import pyautogui
import threading
from LaptopKeyboard import *
import time
from pathlib import Path
import cv2

# Define the region (left, top, width, height)
region = (1333, 930, 20, 20)  

keyboard_thread = threading.Thread(target=lambda: Listener(on_press=on_press, on_release=on_release).start())
keyboard_thread.daemon = True
keyboard_thread.start()  

def compare_images(screenshot_path, reference_path):
    """
    Compare a screenshot with a reference image using template matching.
    Returns the match result score and top-left coordinates of the best match.
    """
    # Read the images
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)
    reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(screenshot, reference, cv2.TM_CCOEFF_NORMED)

    # Find the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val  # Return the best match score and its location

targetWeapon = 0
currentWeapon = 0

key = {"blue_bullet.png": 0, "blue_bomb.png": 1, "blue_fire.png": 2, "red_bullet.png": 0, "red_bomb.png": 1, "red_fire.png": 2,}

while True:
  time.sleep(0.01)
  if get_key_state("r"):
    targetWeapon = 0
  if get_key_state('v'):
    targetWeapon = 1
  if get_key_state('b'):
    targetWeapon = 2
  
  if (get_key_state("b") or  get_key_state('r') or get_key_state('v')):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot.png")
    currentWeapon = -1
    for file in Path("pics").iterdir():
      res = compare_images(screenshot_path="screenshot.png", reference_path=str(file))
      if (res > 0.9): # Check the confidence level
        currentWeapon = key[file.name]
        break
    # print(f"{currentWeapon} {targetWeapon}")
    if (currentWeapon != -1): # Ensure we found a match!
      while (currentWeapon != targetWeapon):
        pushWeaponButton()
        currentWeapon = currentWeapon + 1
        if currentWeapon > 2:
          currentWeapon = 0
    else:
      print("error didnt find")
        
    
    
    
    