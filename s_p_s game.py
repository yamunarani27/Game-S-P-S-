import random

player1_score=player2_score=0
play_count=1

print("Let us start the game")
while(play_count<=3):

    player1=input("Enter ur choice stone/paper/scissor:")
    player2=random.choice(["stone","paper","scissor"])
    print(player2)
    if player1==player2:
        print("Both are in tie")
    elif ((player1=="stone") and (player2=="scissor")) or ((player1=="paper") and (player2=="stone")) or ((player1=="scissor") and (player2=="paper")):
        player1_score +=1
    else:
        player2_score +=1        
    play_count+=1
    
print("player1's score :",player1_score)
print("player2's score :",player2_score)
