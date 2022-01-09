from pytube import Search
from selection import selection
# def func
def init():
  ask = input("Download by video title or url? (title/ url) ")
  if ask.lower() == "title":
    title = input("Title: ")
    s = Search(title)
    url = str(s.results[0])
    url = url[-12:-1]
    url = ("https://www.youtube.com/watch?v={}".format(url))
    var = selection(url) 
    if var == 1:
      print("Invalid link. ")
      init()

    elif var == 0:
      again()
  elif ask.lower() == "url":
    url = input("Url: ")
    if var == 1:
      print("Invalid link. ")
      init()

    elif var == 0:
      again()

  else:
    print("I do not understand. ")
    init()

def again():
  again = input("Do you want to download another youtube video? (yes/ no) ")
  if again.lower() == "yes" or again.lower() == "y":
    init()
  if again.lower() == "no" or again.lower() =="n":
    print("Goodbye!")

init()
