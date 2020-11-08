import random

player1=random.randint(1,100)
trial_count=1

print("Let us start the game")
print(player1)

while(trial_count<=3):

    player2=int(input("Enter a number from 1-99:"))
    if player1>player2:
        print("value is  higher than your guess")
    elif player1<player2:
        print("value is less than your guess")
    else:
        print("your guess is right")
        break
        
    trial_count+=1
    
else:
    print("your trials are over")
