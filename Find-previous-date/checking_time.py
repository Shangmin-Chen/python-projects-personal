import pytz
import datetime

def check_six():
  est = pytz.timezone('US/Eastern')
  now = datetime.datetime.now().astimezone(est)

  current_time = now.strftime("%H")
  if current_time == "09":
    return 0
  else:
    return 1

def check_day():
  est = pytz.timezone('US/Eastern')
  now = datetime.datetime.now().astimezone(est)
  
  d = now.strftime("%d")
  m = now.strftime("%m")
  y = now.strftime("%Y")

  return m, d, y

def check_leap():
  est = pytz.timezone('US/Eastern')
  now = datetime.datetime.now().astimezone(est)
  y = now.strftime("%Y")
  
  if int(y) % 4 == 0:
    # leap year, 29 days in feburary
    return 29
  else:
    # not a leap year, 28 days in feburary
    return 28