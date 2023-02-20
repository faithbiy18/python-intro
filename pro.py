#program to print the largest of the three numbers. Prompt the user to enterthe three numbers 53 10 40
num1=int(input("enter the first numbers:"))
num2=int(input("enter the second numbers:"))
num3=int(input("enter the third numbers:"))
if(num1>num2 and num3):
   print("num1 is the greatest")
elif(num2>num1 and num3):
    print("num2 is the greatest")
elif (num3>num1 and num2):
    print("num3 is the greatest")
    
    
    
"""ask the user for their salary and yrs of service & print the net bonus amount
    #time period of service    bonus
    #more than 10yrs           10%
    #>=6 and <=10              8%
    #less than 6yrs            5% """
    
salary=int(input("Enter the salary:"))
period=int(input("Enter the time period of service:"))
if(period>10):
    net_bonus_amount=salary+(salary*0.10)
elif(period>=6 and period<=10):
    net_bonus_amount=salary*(salary*0.08)
    print("net bonus amount is",net_bonus_amount)
else:
    (period<6)
    net_bonus_amount=salary+(salary*0.05)
    print("net bonus amount is",net_bonus_amount)
    
    
    
