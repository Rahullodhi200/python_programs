import random
lowwer=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
x=random.randint(lowwer,upper)
print("level 1(you have 3 chance")
i=1
while i<=3:
    guess=int(input("guess the no."))
    if x == guess:
        print("no. is ",guess)
    elif x>guess:
        print("no. is too small")
    else:
        print("no. is too large")
    i=i+1
print("level 2(you have 2 chance")
i=1
while i<=2:
    guess=int(input("guess the no."))
    if x == guess:
        print("no. is ",guess)
    elif x>guess:
        print("no. is too small")
    else:
        print("no. is too large")
    i=i+1
print("level 3(you have 1 chance")
i=1
while i<=1:
    guess=int(input("guess the no."))
    if x == guess:
        print("no. is ",guess)
    elif x>guess:
        print("no. is too small")
    else:
        print("no. is too large")
    i=i+1

