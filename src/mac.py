import pyautogui
import os
import sys
import re
from pynput.keyboard import Key, Listener
import time
from random import randint

def process_char(char):
    if char == '<':
        pyautogui.hotkey("shift", ",")
    else:
        pyautogui.write(char)

def launch_temrinal():
    return os.system('open -a Terminal')

def fullscreen():
    pyautogui.press("f11")

def save_file(commands):
    for command in commands:
        pyautogui.hotkey(*command)

def set_command(command, interval=0):
    for char in command:
        process_char(char)
    pyautogui.press("enter")

def is_valid_file(filename):
    if os.path.isdir(filename) or os.path.splitext(filename)[1] == '':
        return False
    elif not os.path.exists(filename):
        return False
    return True

class Autotyper:
    TYPE_SPEED = (0.0, 0.01, 0.05, 0.1)
    AVILABLE_SPEED_COUNT = len(TYPE_SPEED)
    def __init__(self, file_path, output_filename, speed=0):
        if not is_valid_file(file_path):
            print("File path doesnt exist\nQuitting....")
            sys.exit()
        try:
            speed = abs(int(speed))
        except ValueError:
            print("Expected integer")
            sys.exit()
        
        self.file = open(file_path, mode='r')
        self.output_file = output_filename.strip() + os.path.splitext(file_path)[1]
        self.start = False
        self.listener = None
        self.speed = speed % self.AVILABLE_SPEED_COUNT if speed < 4 else random.choice(self.TYPE_SPEED)

        self.save_commands = [ ['ctrl', 's'], ['ctrl', 'x'] ]

    def type_file_content(self, interval):
        while a := self.file.readline():
            indexs_lt_braces = list( map( lambda x: x.span(), list(re.finditer('<', a))) )
            if indexs_lt_braces:
                start = 0
                for index_1, index_2 in indexs_lt_braces:
                    pyautogui.write(a[start:index_1])
                    pyautogui.hotkey("shift", ",") 
                    start = index_2
                pyautogui.write(a[start:], interval)
            else:
                pyautogui.write(a, interval)

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

        fullscreen()
        set_command(f"nano {self.output_file}")
        self.type_file_content(self.speed)
        save_file(self.save_commands)
        self.destruct()

    def destruct(self):
        self.file.close()

