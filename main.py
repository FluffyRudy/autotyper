#!/home/rudy/Documents/autotyper/env/bin/python3.11

from src import mac, linux
import platform
import sys
import threading
from pynput import keyboard

listener = None

def on_press(key):
    if key == keyboard.Key.esc:
        print("Esc key pressed. Stopping...")
        linux.Autotyper.is_inturrepted = True
        listener.stop()

def listen_for_esc_key():
    global listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    print("Press enter to continue:")

    if len(sys.argv) < 3:
        print("No file provided")
        sys.exit()
    print(sys.argv)
    if platform.system() == 'Linux':
        out = linux.Autotyper(*sys.argv[1:])
    elif platform.system() == "Darwin":
        out = mac.Autotyper(*sys.argv[1:])
    else:
        print("Unknow system")
        sys.exit()

    out.run()

if __name__ == "__main__":
    listener_thread = threading.Thread(target=listen_for_esc_key)
    listener_thread.start()
    main()
