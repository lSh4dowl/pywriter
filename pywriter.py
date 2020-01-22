import time
import random
import argparse
import sys
import os
import subprocess
import threading

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try: 
    from pynput import keyboard
except ImportError:
    try:
        install("pynput")
        from pynput import keyboard
    except:
        raise
        sys.exit(0)
runlock = threading.Lock()

running = False

def on_release(key):
    if key == keyboard.Key.f4:
        # Stop program
        print("bye")
        os._exit(0)
    elif key == keyboard.Key.f6:
        # Pause program
        print("pause")
        with runlock:
            global running
            if running:
                running = False
            else:
                running = True

_keyboard = keyboard.Controller()

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=False, default=sys.argv[0])
parser.add_argument("--timeout", "-t", type=int, required=False, default=0)
parser.add_argument("--maxtime", "-M", type=int, required=False, default=150)
parser.add_argument("--mintime", "-m", type=int, required=False, default=50)
parser.add_argument("--raw", "-r", action="store_const", const=True, default=False)
parser.add_argument("--license", "-l", action="store_const", const=True, default=False)

args = parser.parse_args()

_file = args.file
_timeout = args.timeout
_maxtime = args.maxtime
_mintime = args.mintime
_raw = args.raw
_license = args.license

listener = keyboard.Listener(
    on_release=on_release)
listener.start()

if _license:
    print("Pynput | License: https://github.com/moses-palmer/pynput/blob/master/COPYING.LGPL")
    os._exit(0)

print("Press F6 to start. Press F6 again to pause and unpause.")
print("Press F4 to exit.")

time.sleep(_timeout)
with open(_file) as _input:
    for line in _input:
        for char in line:
            while True:
                with runlock:
                    if running:
                        break
                    else:
                        time.sleep(0.01)
                
            if char == '\n':
                if not _raw:
                    _keyboard.press(keyboard.Key.esc)
                    _keyboard.release(keyboard.Key.esc)
                _keyboard.press(keyboard.Key.enter)
                _keyboard.release(keyboard.Key.enter)
                _keyboard.press(keyboard.Key.home)
                _keyboard.release(keyboard.Key.home)
            else:
                _keyboard.press(char)
                _keyboard.release(char)
                randtime = random.randint(_mintime, _maxtime)
                randtime = randtime * 0.001
                time.sleep(randtime)