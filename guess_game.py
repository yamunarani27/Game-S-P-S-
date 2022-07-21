import random

secret_number=random.randint(1,11)

print("Welcome to the guess game!!!!You have 3 chances to guess the right number")
for i in range(1,4):
    number=int(input("enter your guess between 1 to 10:"))
    if i==3:
       print("your guessess are over,the secret number is"+str(secret_number))
       break
    if (number == secret_number):
        print("Congrats,your guess is right!!!!")
        break
    elif(number<secret_number):
        print("Try with a number greater than the guessed number")
    else:
        print("Try with a number lesser than the guessed number")

    
# for i in range (1,4):
#     number=int(input("enter your guess between 1 to 10:"))
#     if (number == secret_number):
#         print("Congrats,your guess is right!!!!")
#         break
#     else:
#         if i==3:
#             print("sorry,your guessess are wrong.The secret number is "+str(secret_number))
#         elif(number<secret_number):
#             print("Try with a number greater than the guessed number")
#         else:
#             print("Try with a number lesser than the guessed number")

