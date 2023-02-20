""" score         Grade
             70-100          A
             60-69           B
             50-59           C
             40-49           D
             0-39            Fail
1.prompt the user to enter 3 units
2.calculate the average
3.grade the average score using the grading system 
"""
    
sub1=int(input("enter first unit:"))
if sub1 < 0:
    raise ValueError("negative value not allowed!")
sub2=int(input("enter second unit:"))
if sub2 < 0:
    raise ValueError("negative value not allowed!")
sub3=int(input("enter third unit:"))
if sub2 < 0:
    raise ValueError("negative value not allowed!")
    
avg = (sub1+sub2+sub3)/3
    
if (avg >= 70 and avg <= 100):
    print("grade A")
elif (avg >= 60  and avg <= 69):
    print("grade B")
elif (avg >= 50 and avg <= 59):
    print("grade C")
    print("grade C")
elif (avg >= 40 and avg <= 49):
    print("grade D")
elif (avg >= 0 and avg <= 39):
    print("Fail")
