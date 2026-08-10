# ----------<{ Copy_Type }>----------

# -----< Libraries >-----

import os
import threading
import pyperclip
import time
import keyboard
import easyocr
import platform

# -----< Functions >-----

def Input_1():
    print("\n---> Ones check your clipboard for the recent copied text")
    speed = input("Enter the speed of typing (1 - 10): ")
    if not speed.isdigit() or not (1 <= int(speed) <= 10):
        print("Invalid speed. Please Restart the program and enter a number between 1 and 10")
        return
    mode = input("Enter the mode (1 : Normal mode, 2 : Coding mode): ")
    if mode == "1":
        print("You have 5 seconds until auto-typing recent copied text from the clipboard\n")
        time.sleep(1)
        for i in range(5, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)
        clipboard_text = pyperclip.paste()
        keyboard.write(clipboard_text, delay=0.1 / float(speed))
    elif mode == "2":
        print("You have 5 seconds until auto-typing recent copied text from the clipboard\n")
        time.sleep(1)
        for i in range(5, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)
        clipboard_text_line = pyperclip.paste().splitlines()
        for i, line in enumerate(clipboard_text_line):
            keyboard.write(line, delay=0.1 / float(speed))
            if i < len(clipboard_text_line) - 1:
                keyboard.send("enter")
                keyboard.send("home")
                keyboard.send("home")
        os._exit(0)
    else:
        print("Invalid mode. Please restart the program and enter a valid mode")
        return
    

def Input_2():
    speed = input("Enter the speed of typing (1 - 10): ")
    if not speed.isdigit() or not (1 <= int(speed) <= 10):
        print("Invalid speed. Please Restart the program and enter a number between 1 and 10")
        return
    try:
        reader = easyocr.Reader(['en'])
        image_path = input("Enter the name of the image with extension (image should be in the same Folder of the script): ")
        text_lines = reader.readtext(image_path, detail=0)
        extracted_text = "\n".join(text_lines)
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return

    print("You have 5 seconds until auto-typing the extracted text from the image\n")
    time.sleep(1)
    for i in range(5, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)
    keyboard.write(extracted_text, delay=0.1 / float(speed))
    os._exit(0)

def Input_3():
    speed = input("Enter the speed of typing (1 - 10): ")
    if not speed.isdigit() or not (1 <= int(speed) <= 10):
        print("Invalid speed. Please Restart the program and enter a number between 1 and 10")
        return
    print("You have 5 seconds to select/highlight the text you want to capture")
    for i in range(5, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)
    try:
        previous_clip = pyperclip.paste()
    except Exception:
        previous_clip = None
    try:
        if platform.system() == 'Darwin':
            keyboard.press_and_release('command+c')
        else:
            keyboard.press_and_release('ctrl+c')
        time.sleep(0.2)
        selected_text = pyperclip.paste()
    except Exception as e:
        print(f"Could not capture selection: {e}")
        return
    if not selected_text:
        print("No text was captured. Make sure you had text selected and try again.")
        return
    try:
        if previous_clip is not None:
            pyperclip.copy(previous_clip)
    except Exception:
        pass
    print("Captured text. You have 5 seconds to focus the target window for typing")
    for i in range(5, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)
    keyboard.write(selected_text, delay=0.1 / float(speed))
    os._exit(0)

def listen_for_stop():
    keyboard.wait('esc')
    print("\n[!] Successfully stopped the program")
    os._exit(0)

#------< Main >-----

if __name__ == "__main__":
    print("<--------------------<{ Copy_Type }>-------------------->\n")
    print("---> Press 'Esc' to stop the program at any time\n")
    print("1. Type the recent copied text from the clipboard in 5 seconds")
    print("2. Type the extracted text from an image in 5 seconds")
    print("3. Type the currently selected/highlighted text in 5 seconds")
    Input = input("Enter Serial Number: ")
    if Input == "1":
        automation_thread = threading.Thread(target=Input_1)
        automation_thread.daemon = True
        automation_thread.start()
        listen_for_stop()
    elif Input == "2":
        automation_thread = threading.Thread(target=Input_2)
        automation_thread.daemon = True
        automation_thread.start()
        listen_for_stop()
    elif Input == "3":
        automation_thread = threading.Thread(target=Input_3)
        automation_thread.daemon = True
        automation_thread.start()
        listen_for_stop()
    else:
        print("Invalid Input. Please restart the program and enter a valid serial number")