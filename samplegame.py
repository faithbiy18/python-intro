# program game from numpy import random
from numpy import random

winning_number = random.randint(0,50)
num=int(input("gues any number:"))
if num==winning_number:
    print("you won")
elif num<winning_number:
    print("the value is too low")
elif num>winning_number:
    print("the value is too high")    
