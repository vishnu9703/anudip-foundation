Sub1=int(input("Enter marks for Sub_1:"))
Sub2=int(input("Enter marks for Sub_2:"))
Sub3=int(input("Enter marks for Sub_3:"))
Sub4=int(input("Enter marks for Sub_4:"))
Sub5=int(input("Enter marks for Sub_5:"))
Total=Sub1+Sub2+Sub3+Sub4+Sub5
average=Total/5
print(average)
if average>=90:
    print("Your Grade is : A1")
elif average>=80 and average<90:
    print("Your Grade is : A2")
elif average>=70 and average<80:
    print("Your Grade is : B1")
elif average>=60 and average<70:
    print("Your Grade is : B2")
elif average>=50 and average<60:
    print("Your Grade is : C1")
elif average>=40 and average<50:
    print("Your Grade is : C1")
elif average>=34 and average<40:
    print("Your Grade is : D")
else:
    print("Ooohh Sorry you are FAIL..!!")