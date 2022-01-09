import webbrowser
from pyautogui import press, click, typewrite
from time import sleep, time
from data import school, email, name
# 13 inch Mac book pro. Default browser = safari.
# Easy level botting.


window = input("Do you have safari opened already? skip if opened, type n if not opened. ")

if window == "n":
    webbrowser.open("https://google.com")
    print("please put it on full screen")

print("Running...")
start = time()


def RUN(email, fname, lname, school):
    webbrowser.open("https://healthscreening.schools.nyc/?type=G")
    sleep(1)

    # click im a student
    click(x=467, y=379)

    # fill first name and last name
    click(x=496, y=506)
    typewrite(fname)
    click(x=781, y=508)
    typewrite(lname)
    click(x=721, y=584)
    typewrite(email)
    click(x=717, y=663)
    sleep(0.5)
    typewrite(school)
    sleep(0.8)
    press("enter")
    click(x=711, y=812)
    sleep(0.3)
    click(x=352, y=428)
    sleep(0.3)
    click(x=354, y=587)
    sleep(0.3)
    click(x=353, y=705)
    sleep(0.3)
    click(x=715, y=762)


for i in range(len(name)):
    names = name[i].split()
    RUN(email[i], names[0], names[1], school)


end = time()
total_run_time = end - start
print("Finished")
print("Total run time: " + str(total_run_time))
