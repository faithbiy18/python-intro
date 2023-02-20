"""ask the user for their salary and yrs of service & print the net bonus amount
    #time period of service    bonus
    #more than 10yrs           10%
    #>=6 and <=10              8%
    #less than 6yrs            5% """
    
period=float(input("enter time period of service:"))
salary=float(input("enter the bonus:"))
if(period > 10):
    print ("bonus is 0.1*salary")
elif(period>=6 and period <=10):
    print ("bonus is 0.08*salary")
elif(period < 6):
    print ("bonus is 0.05*salary")