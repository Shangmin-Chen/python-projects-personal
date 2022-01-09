import requests
from bs4 import BeautifulSoup
import re
# ------------------ scrapes
# --------- this site has the information for all macbooks despite ending in /13-inch it has /14-inch an /16-inch information as well 

site = requests.get("https://www.apple.com/shop/buy-mac/macbook-pro/13-inch")
soup = BeautifulSoup(site.content, 'html.parser')
 
with open("content.txt", "w") as writer:
  writer.write(soup.prettify())

# ------------------- lists
macs = ["mac-product-summary-13inch-entry-0", "mac-product-summary-13inch-good-0",
"mac-product-summary-14inch-better-0",
"mac-product-summary-14inch-best-0",
"mac-product-summary-16inch-better-0",
"mac-product-summary-16inch-best-0",
"mac-product-summary-16inch-ultimate-0",
]
# ------------------- classes
class computer:
  def __init__(self, name, CPU, GPU, RAM, storage, display, price):
    self.name = name
    self.CPU = CPU
    self.GPU = GPU
    self.RAM = RAM
    self.storage = storage
    self.display = display
    self.price = price
  def print_specs(self):
    print("\nItem: {}".format(self.name))
    print("\nCPU: {}\nGPU: {}\nRAM: {}\nStorage: {}\nDisplay: {}\nPrice: {}".format(self.CPU,self.GPU,self.RAM,self.storage,self.display,self.price))
 
class macbookpro13(computer):
  def __init__(self, name, CPU, GPU, RAM, storage, display, price):
    computer.__init__(self, name, CPU, GPU, RAM, storage, display, price)
class macbookpro14(computer):
  def __init__(self, name, CPU, GPU, RAM, storage, display, price):
    computer.__init__(self, name, CPU, GPU, RAM, storage, display, price)
class macbookpro16(computer):
  def __init__(self, name, CPU, GPU, RAM, storage, display, price):
    computer.__init__(self, name, CPU, GPU, RAM, storage, display, price)
 
# ------------ read scrapes using liner search and sorting them into the classes
 
with open("content.txt", "r") as reader:
  for line in reader:
    for j in range(len(macs)):
      if re.search(macs[j], line):
        for i in range(50):
          newlines = next(reader)
          if "CPU" in newlines.split():
            CPU = newlines.strip()
          if "GPU" in newlines.split():
            GPU = newlines.strip()
          if "memory" in newlines.split():
            RAM = newlines.strip()
          if "storage" in newlines.split():
            storage = newlines.strip()
          if "display" in newlines.split():
           display = newlines.strip()
          if 'class="as-price-currentprice"' in newlines.split():
            for a in range(2):
              price = next(reader).strip()

            if j == 0:
              onepro13 = macbookpro13("MacBook Pro 13 v1",CPU, GPU,RAM,storage, display, price)
            elif j == 1:
              twopro13 = macbookpro13("MacBook Pro 13 v2",CPU, GPU,RAM,storage, display, price)
            elif j == 2:
              onepro14 = macbookpro14("MacBook Pro 14 v1",CPU, GPU,RAM,storage, display, price)
            elif j == 3:
              twopro14 = macbookpro14("MacBook Pro 14 v2",CPU, GPU,RAM,storage, display, price)
            elif j == 4:
              onepro16 = macbookpro16("MacBook Pro 16 v1",CPU, GPU,RAM,storage, display, price)
            elif j == 5:
              twopro16 = macbookpro16("MacBook Pro 16 v2",CPU, GPU,RAM,storage, display, price)
            elif j == 6:
              threepro16 = macbookpro16("MacBook Pro 16 v3",CPU, GPU
              ,RAM,storage, display, price)
 
# ----- user input and selection
def run():
  ask = input("Which Macbook Pro are you looking for? 13 inch, 14 inch, or 16 inch?: ")

  if ask == "13" or ask.lower() == "13 inch":
    ask2 = input("\nWhich verison do you want? 1 or 2: ")
    if ask2 == "1":
      onepro13.print_specs()
    elif ask2 == "2":
      twopro13.print_specs()
    else:
      print('\nI dont understand, please input either "1" or "2"\n')
      run()
  elif ask == "14" or ask.lower() == "14 inch":
    ask2 = input("\nWhich verison do you want? 1 or 2: ")
    if ask2 == "1":
      onepro14.print_specs()
    elif ask2 == "2":
      twopro14.print_specs()
    else:
      print('\nI dont understand, please input either "1" or "2"\n')
      run()
  elif ask == "16" or ask.lower() == "16 inch":
    ask2 = input("\nWhich verison do you want? 1, 2 or 3: ")
    if ask2 == "1":
      onepro16.print_specs()
    elif ask2 == "2":
      twopro16.print_specs()
    elif ask2 == "3":
      threepro16.print_specs()
    else:
      print('\nI dont understand, please input either "1" or "2"\n')
      run()
  else:
    print('\nI dont understand, please input either "13 inch", "14 inch", or "16 inch"\n')
    run()

run()