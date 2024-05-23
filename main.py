import random
from art import logo,vs
from game_data import data
from replit import clear


#Checks who the winner is
win = ""
def winner(name_a, name_b):
    global win
    if name_a['follower_count'] > name_b['follower_count']:
        win = 'a'
    else:
        win = 'b'
    return win
    


#Gets a random name from the list for both A and B
name_a = random.choice(data)
name_b = random.choice(data)
cont = True
print(logo)
score = 0
while cont == True:
    print(f"Compare A: {name_a['name']}, a {name_a['description']}, from {name_a['country']}")
    print(vs)
    print(f"Against B: {name_b['name']}, a {name_b['description']}, from {name_b['country']}")
    pick_letter = input("Who as more followers? Type 'A' or 'B': ").lower()
    winner(name_a, name_b)
    if pick_letter == win:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
        
        name_a = name_b
        name_b = random.choice(data)
    else:
        clear()
        print(f"Sorry that's wrong,final score: {score}")
        cont = False
