from random import randint


print("Practice Squares from 1 to 20\n")
for i in range(1,21):

    a=randint(1,21)
    print(a)
    #print("Please enter yoour answer below\n")
    b=int(input("\nPlease enter yoour answer\n"))
    print(a,"=",+b)
    if(b==a*a):
        print("\nWow! Your answer is CORRECT")
    else:
        print("\nYour answer is wrong")
        print("Correct answer is: \n")
        print(a*a)
        print("\nBetter Luck Next time")
    