import random
import time

print("Hangman game".center(130,'*'))
print("Welcome to the game")
time.sleep(1)

file=open(r"Words.txt",'r')
words=file.readlines()

word=words[random.randint(0,len(words)-1)]
word.strip();
n=len(word)

ans=list('_'*(n-1))
chance = 7
print("\nThe words is",end=" ")
print(" ".join(ans))

while(chance>0):
    p=False
    r=False

    print("\nGuess the letter(a-z):",end=" ")
    guess=input()
    time.sleep(0.5)

    if(len(guess)!=1):
        print("Invalid guess\nTry again!!!")
        continue

    for i in range(n):
        if(word[i]==guess):
            if(ans[i]!='_'): r=True
            ans[i]=guess
            p=True
            
    if(not p):
        chance-=1
        print("Sorry", guess ,"is not present")
        print("Life left= ",chance)       
    else:
        if(not r):
            print("Yes",guess, "is present")
            print("\nThe word is",end=" ")
            print(" ".join(ans))
        else:
            print(guess," is alread found try another letter")


    if(ans.count('_')==0):   
        print("You found the correct word")
        print("Winner !!!")
        break
    
if(chance==0):
            print("\nGame over")
            print("The correct word is: ",word)
            print("Try again")
      


