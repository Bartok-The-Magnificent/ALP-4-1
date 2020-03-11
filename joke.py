from random import *

file = open("joke.txt", "r")
print(file.read(randint(0,len(file.readlines())-1)))