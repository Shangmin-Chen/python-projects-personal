# this is a library that I want to make because a lot of my programs are automation bots and find previous date will be important

from checking_time import check_day, check_leap

def update_list():
  feb = check_leap()
  global mtod
  mtod = {"1": 31, "2": feb, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}

update_list()

m, d, y = check_day()

print(m,d,y)

def recur():
  global back
  back = input("how many days back? ")
  try:
    back = int(back)
  except ValueError:
    print("try again")
    recur()

recur()

m, d, y = int(m), int(d), int(y)

for i in range(int(back)):
  d -= 1
  if d == 0:
    m -= 1
    if m == 0:
      m = 12
      y -= 1
      update_list()
      d = mtod[str(m)]
    else:
      d = mtod[str(m)]
      
print(m, d, y)
