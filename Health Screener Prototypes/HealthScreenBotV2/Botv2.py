import requests
from data import name, email
from time import time
url = "https://healthscreening.schools.nyc/home/submit"
start = time()

def RUN(email, fname, lname):
    data = {
        "Type": "G",
        "IsOther": "False",
        "IsStudent": "1",
        "FirstName": fname,
        "LastName": lname,
        "Email": email,
        "State": "NY",
        "Location": "R605",
        "Floor": "",
        "Answer1": "0",
        "Answer2": "0",
        "Answer3": "0",
        "ConsentType": "",
    }

    response = requests.post(url, data=data).text
    print(response)


for i in range(len(name)):
    names = name[i].split()
    RUN(email[i], names[0], names[1], )


end = time()
total_run_time = end - start
print("\nFinished")
print("Total run time: " + str(total_run_time))
