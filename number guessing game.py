import random
chance=5
a =random.randint(1,15)
print("Guess a number (between 1 and 15):")  
while chance!=0: 
    b = int(input())
    if a==b:
        print("Congratulation YOU WON!!!") 
        break
    else:
        print("try again")
    chance=chance-1
print("game over")

