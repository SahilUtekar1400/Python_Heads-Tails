import random

heads ='''
 /$$   /$$                           /$$          
| $$  | $$                          | $$          
| $$  | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$$
| $$$$$$$$ /$$__  $$ |____  $$ /$$__  $$ /$$_____/
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$|  $$$$$$ 
| $$  | $$| $$_____/ /$$__  $$| $$  | $$ \____  $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/
|__/  |__/ \_______/ \_______/ \_______/|_______/ 
'''
tails ='''
$$$$$$$$\        $$\ $$\           
\__$$  __|       \__|$$ |          
   $$ | $$$$$$\  $$\ $$ | $$$$$$$\ 
   $$ | \____$$\ $$ |$$ |$$  _____|
   $$ | $$$$$$$ |$$ |$$ |\$$$$$$\  
   $$ |$$  __$$ |$$ |$$ | \____$$\ 
   $$ |\$$$$$$$ |$$ |$$ |$$$$$$$  |
   \__| \_______|\__|\__|\_______/ 
'''

coin_face = [heads,tails]

computer_choice = random.randint(0,1)
print("Welcome to the game of chance!")
user_choice = int(input("Choose your option Heads or Tails? Enter '0 for Heads' & '1 for Tails'?"))

if user_choice == computer_choice:
    print("You chose\n" + coin_face[user_choice])
    print("Computer chose\n" + coin_face[computer_choice])
    print("you win!")

elif user_choice >= 2:
    print("You chose a invalid input detail- \"You Loose\"")

else:
    print("You chose\n" + coin_face[user_choice])
    print("Computer chose\n" + coin_face[computer_choice])
    print("You Loose")