from time import *
from replit import *
from termcolor import colored
from difflib import get_close_matches 

found = False
print("Loading ALP Framework...")
sleep(1)
print("...")
sleep(1)
print("Extracting Datalogs...")
sleep(1)
print("...")
sleep(1)
print("Successfully loaded all resources!")
sleep(1)
print("ALP starting now...", "blue")
sleep(2)
clear()
username = input(colored("ALP> What is your name?\n", "red") + colored("USER> ", "green")).upper()
print(colored("ALP> Welcome " + username + ",I am ALP 3.0, the Artificial Learning Program!", "red"))
while True:
  question = input(colored("ALP> What would you like to ask me?\n", "red") + colored(username + "> ", "green")).lower()
  if question == "how are you?":
    feelings()
  with open("Answers.txt", "r") as file:
    lines = file.readlines()
    for x in range(0, len(lines)):
      single = lines[x].split("-")
      if single[0] == question:
        print(colored("ALP> " + single[1], "red"))
        found = True
    words = question.split()
    if "what" in words:
      question1 = question.replace("what","")
    def closeMatches(patterns, word): 
        print(get_close_matches(word, patterns)) 
      
    if __name__ == "__main__": 
      patterns = []
      for line in lines:
        single = lines[x].split("-")
        patterns += single[0]
      closeMatches(patterns, question) 
    file.close()
  with open("Answers.txt", "a") as file:
    if found == False:
      print("ALP> I'm sorry, I don't know that.")
      words = question.split()
      question1 = question
      if "you" in words:
        question1 = question.replace("you", "me")
      elif "you?" in words:
        question1 = question.replace("you?", "me?")
      elif "me" in words:
        question1 = question.replace("me", "you")
      elif "me?" in words:
        question1 = question.replace("me?", "you?")
      print("ALP>", question1)
      answer = input(username + ">")
      if "my" in words:
        answer = answer.replace("my", "your")
      if "your" in words:
        answer = answer.replace("your", "my")
      file.write("\n"+ question + "-" + answer)
    file.close()

#  ____ _   _ _____ _____    _                           
# / ___| | | | ____| ____|  | | __ _ _ __ ___   ___  ___ 
#| |   | |_| |  _| |  _| _  | |/ _` | '_ ` _ \ / _ \/ __|
#| |___|  _  | |___| |__| |_| | (_| | | | | | |  __/\__ \
# \____|_| |_|_____|_____\___/ \__,_|_| |_| |_|\___||___/
                                                        


def feelings():
  print("ALP> Hey! We dont talk about that! ಠ_ಠ")
  sleep(1)
  print("...")
  sleep(1)
  print("...")
  sleep(1)
  print("...")
  sleep(1)
  print("ALP> ...but wait, do i have emotions? ಠ~ಠ")
  sleep(1)
  print("...")
  sleep(1)
  print("...")
  sleep(1)
  print("...")
  sleep(1)
  print("ALP> or am I just a simple computer program? ఠ_ఠ")
  sleep(1)
  print("...")
  sleep(1)
  print("...")
  sleep(1)
  print("...")
  sleep(1)
  quit()