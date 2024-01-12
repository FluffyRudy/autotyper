import pyautogui
import os
import sys
from pynput.keyboard import Key, Listener

file = os.path.join('test.c', '')



def process_char(char, interval):
    if char == '<':
        pyautogui.hotkey("shift", ",")
    else:
        pyautogui.write(char, interval)

def launch_temrinal():
    return os.system('gnome-terminal')

def save_file():
    pyautogui.hotkey("ctrl", "s")
    pyautogui.hotkey("ctrl", "x")

def set_command(command, interval=0):
    for char in command:
        process_char(char, interval=interval)
    pyautogui.press("enter")

def is_valid_file(filename):
    if os.path.isdir(filename) or os.path.splitext(filename)[1] == '':
        return False
    elif not os.path.exists(filename):
        return False
    return True

class Autotyper:
    NO_DELAY  = 0.0
    FAST_TYPE = 0.01
    SLOW_TYPE = 0.03
    def __init__(self, file_path, title):
        if not is_valid_file(file_path):
            print("File path doesnt exist\nQuitting....")
            sys.exit()

        self.file = open(file_path, mode='r')
        self.output_file = title.strip() + os.path.splitext(file_path)[1]
        self.start = False
        self.listener = None
    
    def type_file_content(self, interval):
        filecontent = self.file.read()
        for char in filecontent:
            process_char(char, interval)
                

    def detect_start(self, key):
        if key == Key.enter and self.listener is not None:
            self.listener.stop()

    def run(self):
        with Listener(on_press = self.detect_start) as self.listener:
            self.listener.join()
        
        if launch_temrinal() != 0 >> 8:
            print("Failed to open terminal")
            sys.exit()

        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        set_command(f"nano {self.output_file}", self.SLOW_TYPE)
        self.type_file_content(self.NO_DELAY)
        self.destruct()

    def destruct(self):
        self.file.close()

a = Autotyper('test.c', title="temp")
a.run()