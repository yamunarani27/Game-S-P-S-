import random

computer=["stone","paper","scissor"]
player1_score=player2_score=0
play_count=1

print("Let us start the game")

while(play_count<=10):

    player1=input("Enter ur choice:")

    player2=random.choice(computer)

    print("player2's choice is "+player2)

    if ((player1=="stone") and (player2=="scissor")) or ((player1=="paper") and (player2=="stone")) or ((player1=="scissor") and (player2=="paper")):
        player1_score +=1
    elif ((player1=="paper") and (player2=="scissor")) or ((player1=="scissor") and (player2=="stone")) or ((player1=="stone") and (player2=="paper")):
        player2_score +=1
    else:
        print("Both are in tie")

    play_count+=1
    

print("player1's score is:",player1_score)
print("player2's score is:",player2_score)
