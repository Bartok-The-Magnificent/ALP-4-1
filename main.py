import requests
from time import *
from replit import *
from termcolor import colored
login = False
userfound = False
passwordfound = False

print("Loading ALP Framework...",)
sleep(1)
print("...")
sleep(1)
print("Importing modules..")
sleep(1)
print("Extracting Colors from termcolor module")
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
sleep(0.8)
username = input(colored("ALP> What is your name?\n","red") + colored ("USER> ", "green")).upper()




url = 'https://www.google.com/'
r = requests.get(url)

#  ____ _   _ _____ _____    _                           
# / ___| | | | ____| ____|  | | __ _ _ __ ___   ___  ___ 
#| |   | |_| |  _| |  _| _  | |/ _` | '_ ` _ \ / _ \/ __|
#| |___|  _  | |___| |__| |_| | (_| | | | | | |  __/\__ \
# \____|_| |_|_____|_____\___/ \__,_|_| |_| |_|\___||___/