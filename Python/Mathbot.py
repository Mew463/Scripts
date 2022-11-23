from PIL import Image
from PIL import Image, ImageGrab
import keyboard
import cv2
import numpy as np
import pytesseract
import time

def empty(a):
    pass

def functionthing():
    im2 = ImageGrab.grab(bbox=(4, 731, 487, 923)).save("text.png")
    #MathImage = "sample math question.PNG"
    MathImage = "text.png"
    img = cv2.imread(MathImage)
    HSVImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 255])
    upper = np.array([177, 196, 255])
    mask = cv2.inRange(HSVImage, lower, upper)
    result = 255 - mask
    #cv2.imshow("Mask", mask)
    #cv2.imshow("result", result)
    cv2.imwrite("MaskedImage.jpg", result)
    #cv2.waitKey(1)
    ImageConvert = "MaskedImage.jpg"
    pytesseract.pytesseract.tesseract_cmd = r'D:\PyTesseract\tesseract.exe'
    #f = Image.open(MathImage).show()
    print(pytesseract.image_to_string(Image.open(ImageConvert)))
    print("--------------------------------")
    text = (pytesseract.image_to_string(Image.open(ImageConvert)))
    #text_file = open("sample.txt", "wt")
    #n = text_file.write(pytesseract.image_to_string(Image.open(ImageConvert)))
    if text.find("Math") != -1:
        print("Math found at " + str(text.find('Math')))
        MathPos = text.find("Math")
        print(MathPos)
    else:
        print("Math not Found")
        return
    if text.find("=", MathPos, MathPos + 30) != -1:
        print("Equal sign found at " + str(text.find('=', MathPos, MathPos + 30)))
        EqualPos = text.find("=", MathPos, MathPos + 30)
    else:
        print("Equal sign not found")
        print("Searching for word, > ")
        if text.find(">", MathPos, MathPos + 30) != -1:
            print("Found!")
            print("> found at " + str(text.find('>', MathPos, MathPos + 30)))
            EqualPos = text.find(">", MathPos, MathPos + 30) - 1
        else:
            print("Unable to Find >, Restarting..")
            cv2.imwrite("errorimage.png",result)
            functionthing()
            return

    if text.find("Math") != -1 and EqualPos != 0:
        print("Both Are Found!")
        print("Math problem = " + str(text[text.find('Math') + 6:EqualPos]))
        if text.find("/", MathPos, EqualPos) != -1:
            print("Division")
            Operation = 1
            Operationpos = text.find("/", MathPos, EqualPos)
        if text.find("*", MathPos, EqualPos) != -1:
            print("Multiplication")
            Operation = 2
            Operationpos = text.find("*", MathPos, EqualPos)
        if text.find("-", MathPos, EqualPos) != -1:
            print("Subtraction")
            Operation = 3
            Operationpos = text.find("-", MathPos, EqualPos)
        if text.find("+", MathPos, EqualPos) != -1:
            print("Addition")
            Operation = 4
            Operationpos = text.find("+", MathPos, EqualPos)
        #print("Operator position = " + str(Operationpos))
        try:
            Num1 = int(text[text.find('Math') + 6:Operationpos])
            print(Num1)
        except ValueError:
            print("Error with Num1, Restarting...")
            functionthing()
            return
        try:
            Num2 = int(text[Operationpos + 1:EqualPos])
            print(Num2)
        except ValueError:
            print("Error with Num2, Restarting...")
            cv2.imwrite("errorimage.png", result)
            functionthing()
            return
        if Operation == 1:
            answer = round(Num1 / Num2)
        if Operation == 2:
            answer = Num1 * Num2
        if Operation == 3:
            answer = Num1 - Num2
        if Operation == 4:
            answer = Num1 + Num2
        print(answer)
        keyboard.press_and_release('t')
        time.sleep(0.25)
        keyboard.write(str(answer))
        keyboard.send("enter")
    else:
        return




keyboard.add_hotkey('ctrl+n',functionthing)

keyboard.wait() #Very Important

