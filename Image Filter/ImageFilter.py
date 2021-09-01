import numpy as np
from numba import jit
import cv2, json
from mss import mss
from win32api import GetSystemMetrics
from time import sleep


paused = False
running = False


def load():

    with open("config.json") as json_file:
        config = json.load(json_file)

    return config


@jit
def transform_keep_value(array):

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j][0] = 0
            array[i][j][1] = 0
            # array[i][j][2] = 0


def pause():

    global paused, running

    if running:
        paused = not paused 


def close():

    global running

    running = False
    sleep(0.1)
    cv2.destroyAllWindows()


def run():

    global paused, running, sct

    config = load()

    paused = False
    running = True

    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    bounding_box = {'top': 0, 'left': 0, 'width': x, 'height': y}

    while running:
        if not paused:
            pixel_array = np.array(mss().grab(bounding_box))

            # BGR COLORSPACE
            reduced = np.array([i[::config["resolution_downscale"]] for i in pixel_array[::config["resolution_downscale"]]])
            bgr_reduced = cv2.cvtColor(reduced, cv2.COLOR_BGRA2BGR)

            # HSV 180 255 255
            hsv = cv2.cvtColor(bgr_reduced, cv2.COLOR_BGR2HSV)
            transform_keep_value(hsv)
            bgr_out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

            cv2.imshow('Value', bgr_out)
            cv2.setWindowTitle("Value", "Value")
            cv2.waitKey(1)
        else:
            cv2.setWindowTitle("Value", "Value pause")
            sleep(0.1)
