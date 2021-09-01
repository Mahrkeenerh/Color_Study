from pynput.keyboard import Listener


def on_press(key):

    print(str(key).replace("'", ""))


def run():

    with Listener(on_press=on_press, on_release=None) as listener:
        listener.join()


run()
