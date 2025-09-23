# import random

# def game():
#     print("You are playing a game!!!")
#     score= random.randint(1, 10)
#     with open("game.txt") as file:
#         hiscore= file.read()
#         print(hiscore)
#         if(hiscore!=""):
#             hiscore= int(hiscore)
#         else:
#             hiscore= 0
#     print(f"Your score is: {score}")
#     if(score>hiscore):
#         with open("game.txt", "w") as file:
#             file.write(str(score))
#     return score



import random
def game():
    print("You are playing a game!!!")
    score= random.randint(1, 100)
    with open("game.txt") as file:
        hiscore= file.read()
        print(hiscore)
        if(hiscore!=""):
            hiscore= int(hiscore)
        else:
            hiscore= 0
    
    print(f"Your sxcore is: {score}")
    if(score>hiscore):
        with open("game.txt", "w") as file:
            file.write(int(score))
        return score
        
