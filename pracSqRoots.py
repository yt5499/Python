from cmath import sqrt
from random import Random, randint, random
def gri():
    return t[randint(0,len(t)-1)]

print("Practice Square Roots from 1 to 20\n")
t=(1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400)

for i in range(1,50):
    c=gri()
    print(c)

    a=sqrt(c)
    
    b=int(input("\nEnter your answer\n"))

    if(b==a):
        print("Great! Your answer is CORRECT\n")

    else:
        print("Sorry! Your answer is wrong")
        print("Correct answer is: ",+a)