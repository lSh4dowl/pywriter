import time
import random
import argparse
import sys
import os
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try: 
    from pynput.keyboard import Key, Controller
    from pynput import keyboard as k
except ImportError:
    try:
        install("pynput")
        from pynput.keyboard import Key, Controller
        from pynput import keyboard as k
    except:
        raise
        sys.exit(0)


def on_press(key):
    pass

def on_release(key):
    if key == k.Key.f4:
        # Stop programm
        print("bye")
        os._exit(0)

listener = k.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("Press F4 to exit.")

keyboard = Controller()

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=False)
parser.add_argument("--timeout", "-t", type=int, required=False)
parser.add_argument("--maxtime", "-M", type=int, required=False)
parser.add_argument("--mintime", "-m", type=int, required=False)
parser.add_argument("--raw", "-r", type=bool, required=False)

args = parser.parse_args()

_file = args.file if args.file != None else sys.argv[0]
_timeout = args.timeout if args.timeout != None else 5
_maxtime = args.maxtime if args.maxtime != None else 150
_mintime = args.mintime if args.mintime != None and args.mintime <= _maxtime else 50
_raw = args.raw if args.raw != None else False

time.sleep(_timeout)
with open(_file) as _input:
    for line in _input:
        for char in line:
            if char == '\n':
                if not _raw:
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                keyboard.press(Key.home)
                keyboard.release(Key.home)
            else:
                keyboard.press(char)
                keyboard.release(char)
                randtime = random.randint(_mintime, _maxtime)
                randtime = randtime * 0.001
                time.sleep(randtime)