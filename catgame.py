# move cursor to one of the corners of the screen to disable code (pyautogui.FAILSAFE)
# this is a code for me to afk farm a cat game I downloaded on my mac for free coins
from pynput import keyboard
from time import sleep
from pyautogui import click


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k == "a":  # keys of interest
        run()

 
def run():
    while True:
        click()
        sleep(2)


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
