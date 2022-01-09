# how i'm trolling my cousin playing a free admin game
# step 1: set up a loop that infinitely spawn kills this guy and ruins his game experience
# step 2: sit next to him while laughing at him dying right as he spawns
from pyautogui import press, keyDown, keyUp
from time import sleep
from pyperclip import copy
target_name = input("target name: ")
kill_command = input("kill command: ")
copy("/e " + kill_command + " " + target_name)

# countdown
count_down = 5
for i in range(5):
    print(count_down - i)
    sleep(1)
print("take off")

# loop
while True:
    press("/")
    keyDown("command")
    keyDown("v")
    keyUp("command")
    keyUp("v")
    press("enter")
    sleep(3.5)
