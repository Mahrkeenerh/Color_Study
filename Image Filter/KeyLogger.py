from pynput.keyboard import Listener
from threading import Thread
import ImageFilter, json


running = False
pressed = {}
pressed_pause = {}
shortcut = []
pause_shortcut = []


def load():

    global shortcut, pressed, pause_shortcut

    with open("config.json") as json_file:
        config = json.load(json_file)

    shortcut = config["shortcut"]
    pause_shortcut = config["pause"]

    for s in shortcut:
        pressed[s] = False


def on_press(key):

    global running, pause_shortcut, shortcut, pressed_pause, pressed

    strip_key = str(key).replace("'", "")

    if strip_key in shortcut:
        pressed[strip_key] = True
    
    if strip_key in pause_shortcut:
        pressed_pause[strip_key] = True

    if all(list(pressed.values())):
        if not running:
            Thread(target=ImageFilter.run).start()
        else:
            ImageFilter.close()
        
        running = not running
    
    if all(list(pressed_pause.values())):
        ImageFilter.pause()


def on_release(key):

    global shortcut, pause_shortcut, pressed, pressed_pause

    strip_key = str(key).replace("'", "")

    if strip_key in shortcut:
        pressed[strip_key] = False
    
    if strip_key in pause_shortcut:
        pressed_pause[strip_key] = False


def run():

    load()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
