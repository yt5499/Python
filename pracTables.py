from random import randint


print("Practice Any Table you want\n")
a=int(input("Enter the Table you want to PRACTICE: \n"))


for i in range(1,11):
    
    print(a,"*",i,"=")
    b=int(input("Enter your Answer here: "))

    if(b==(a*i)):
        print("Your answer is CORRECT\n\n")
    else:
        print("Sorry! Your answer is wrong")
        print("Correct answer is: ",+a*i)
        print("Better Luck next time")