import requests
from time import *
from replit import *
from termcolor import colored
from stolencode import *
from urllib import *
from googlesearch import *
import subprocess
from function1 import *
from dictionaryboi import *

login = False
userfound = False
passwordfound = False
functioncall = 0

print("Loading ALP Framework...",)
sleep(1)
print("...")
sleep(1)
print("Importing modules...")
sleep(1)
print("...")
sleep(1)
print("Extracting Colors from termcolor module...")
sleep(1)
print(colored("...", "red"))
sleep(0.9)
print(colored("...","green"))
sleep(0.9)
print(colored("...", "blue"))
sleep(1)
print(colored("Resources loaded successfully!","green"))
sleep(1)
print(colored("ALP starting now...","green"))
sleep(2)
clear()

print(colored("ALP> Hello USER","red"))
sleep(0.5)
print(colored("ALP> Please log in or create an account:","red"))
sleep(0.8)

MySexyBody()

while functioncall == 0:
  functionchoice = input ("What would you like me to do?\n").lower()
  if functionchoice == ("test"):
    function1()
    functionchoice = ("novalue")
  if functionchoice == ("define"):
    definitionrequest()
    functionchoice = ("novalue")
  if functionchoice == ("web"):
    googlesearch()
    functionchoice = ("novalue")



#  ____ _   _ _____ _____    _                           
# / ___| | | | ____| ____|  | | __ _ _ __ ___   ___  ___ 
#| |   | |_| |  _| |  _| _  | |/ _` | '_ ` _ \ / _ \/ __|
#| |___|  _  | |___| |__| |_| | (_| | | | | | |  __/\__ \
# \____|_| |_|_____|_____\___/ \__,_|_| |_| |_|\___||___/