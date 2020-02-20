# ♤♡♧♢♠♥♣♦

import random
player_cards = []
player_points = []


cards = ["♥A","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥J","♥Q","♥K",
         "♣A","♣2","♣3","♣4","♣5","♣6","♣7","♣8","♣9","♣10","♣J","♣Q","♣K",
         "♦A","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦J","♦Q","♦K",
         "♠A","♠2","♠3","♠4","♠5","♠6","♠7","♠8","♠9","♠10","♠J","♠Q","♠K"]

points = [11,2,3,4,5,6,7,8,9,10,10,10,10,
          11,2,3,4,5,6,7,8,9,10,10,10,10,
          11,2,3,4,5,6,7,8,9,10,10,10,10,
          11,2,3,4,5,6,7,8,9,10,10,10,10]


while(True):
    hit_me = input("Do you want a card? y/n ")
    if (hit_me == "y"):
        card_number = random.randint(0,51)
        player_cards.append(cards[card_number])
        player_points.append(points[card_number])
        print("\nYou have "+' '.join(str(x) for x in player_cards))
        print("You have "+str(sum(player_points))+" points. \n")
        if (sum(player_points) > 21):
            print ("You are busted!")
            break
        
    elif (hit_me == "n"):
        break
    else:
        print("Choose y or n to say if you want a card or not.")
