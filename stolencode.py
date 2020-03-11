def MySexyBody():
  import time,replit
  from termcolor import colored
  global logincomplete
  a = 0
  option = ""
  usernumber = 0
  stuff = []
  key = "XWaqz8SMrvvdiYNe-FqzKmBcheshandSikmHpcniVbc="
  print(colored("ALP> Please Choose An Option:\n1.Sign In\n2.Sign Up","red"))
  option = input(colored("\nUSER> ","green")).lower()

  def LoginBoi():
    global username
    global password
    username = input(str("Username: "))
    password = input(str("Password: "))

  def SignInBois():
    print("Welcome back to ALP!\nPlease enter your username and password:\n")
    LoginBoi()

  def SignUpBois():
    print("Welcome to ALP!\nPlease enter a username and a password:\n")
    username = input("Username: ")
    password = input("Password: ")
    stuff.append(username)
    stuff.append(password)
    with open("SignIn.txt", "a") as f:
      for a in range(0, len(stuff)):  
        word = list(stuff[a])         
        for x in range(0, len(key)): 
          for b in range(0, len(word)):
            word[b] = chr(ord(word[b]) + ord(key[x]))
        stuff[a] = "".join(word)
    with open("SignIn.txt", "a") as f:
      for x in range(0, len(stuff)):
        f.write(stuff[x] + "\n")
    print("Please Sign In:\n")
    LoginBoi()

  if option == "1":
    SignInBois()
  if option == "sign in":
    SignInBois()
  if option == "2":
    SignUpBois()
  if option == "sign up":
    SignUpBois()
    
  def welcome():
    line = "-------" + "-" * len(username)
    print("Hello", username + "!\n" + line)
      

  with open("SignIn.txt", "r") as f:
    thing = f.readlines()

  for x in range(0, len(thing)):
    thing[x] = thing[x][:-1]

  for a in range(0, len(thing)):  
    word = list(thing[a])          
    for x in range(0, len(key)):   
      for b in range(0, len(word)):
        word[b] = chr(ord(word[b]) - ord(key[x]))
    thing[a] = "".join(word)
  good = 0
  a = 0

  while a != len(thing):
    if username == thing[a] and password == thing[a+1]:
      good = 1
      if a == 0:
        usernumber = 0
      else:
        usernumber = a / 2
      usernumber = int(usernumber)
      time.sleep(1)
      welcome()
      f = open("checklogin.txt", "w") #sets checklogin.txt to "true"
      f.write ("true")
      break
    a = a + 2

  if good == 0:
    print("\nYour Password or Username is Incorrect!")
    
#  ____ _   _ _____ _____    _                           
# / ___| | | | ____| ____|  | | __ _ _ __ ___   ___  ___ 
#| |   | |_| |  _| |  _| _  | |/ _` | '_ ` _ \ / _ \/ __|
#| |___|  _  | |___| |__| |_| | (_| | | | | | |  __/\__ \
# \____|_| |_|_____|_____\___/ \__,_|_| |_| |_|\___||___/