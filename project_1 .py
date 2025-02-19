

import random
item = ["Paper","Scissor","Rock"]
user_ip= input("enter your move from 'Rock,Paper,Scissor : ")
bot_choice = random.choice(item)

print("user move :",user_ip)
print()
print("bot move : ",bot_choice)



if(bot_choice == user_ip):
    print(" match is draww... baby")

elif(bot_choice == "Rock" and user_ip== "Paper"):
    print("***** You Win Baby *****")
elif(bot_choice == "Rock" and user_ip == "Scissor"):
    print("Bot Wins, (you loose basically)")
elif(bot_choice == "Paper" and user_ip == "Rock"):
    print("Bot Wins, (you loose basically")
elif(bot_choice == " Paper" and user_ip == " Scissor"):
    print("***** You Win Baby *****")
elif(bot_choice == "Scissor" and user_ip == "Rock"):
    print("***** You Win Baby *****")
elif(bot_choice == "Scissor" and user_ip == "Paper"):
    print("Bot Wins, (you loose basically)")
else:
    print(" Give input correctly Master")
