"""a program that prompts the user to test if a number is divisble by 5 """
num=int(input("Enter a number: "))
if(num%5==0):
    print("The number is divisble by 5")
else:
    print("The number is not divisble by 5")


""" print whether a number is even or odd"""

num=int(input("Enter a number: "))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")

#LOGICAL OPERATORS
""" write a program to check if a person is eligibleto vote or not"""
nationality=input("Enter your nationality: ")
age=int(input("Enter your age: "))
if nationality=="kenyan" and age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
   
   
"""program to implement the following; a bank will offer a loan if they are 21yrs and above and annual income of atleast 21000.
expected output:
1.congratulations if you qualify for a loan 
2.unfortunately we ae unable to offer you a loan at this time"""

age=int("Enter your age: ")
annual_income=int("enter the annual income:") 
if age>=21 and annual_income>=21000:
    print("congratulation for the qualification")
else:
    print("unfortunately we are unable to offer you a loan at this time")
    


    

#RELATIONAL OPERATORS
"""Aprogram to assign a discount of 5% if amount of purchase exceeds ksh1000 """
amount=int(input("Enter the amount of purchase: "))
discount=0.05*amount
if(amount>=1000):
    print("discount is given is:",discount)
else:
    print("discount is not given")

    