# python program 6(hangman)
import time
import random
name = input("what is your name?")
print("hello, " + name, "Time to play hamgman!")
time.sleep(1)
print("start guessing...\n")
time.sleep(0.5)
words=['python','programming','treasure','creative','medium','horror']
word=random.choice(words)
guesses=''
turns=5
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed +=1
    if failed == 0:
            print("\nyou won")
            break
    guess=input("\nguess a character:")
    guesses +=guess
    if guess not in word :
        turns -= 1
        print("\nwrong")
        print("\nyou have", + turns, 'more guesses')
        if turns == 0:
            print("\nyou lose")
            