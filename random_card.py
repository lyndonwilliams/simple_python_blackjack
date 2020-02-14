# ♤♡♧♢♠♥♣♦

import random


cards = ["♥A","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥J","♥Q","♥K",
         "♣A","♣2","♣3","♣4","♣5","♣6","♣7","♣8","♣9","♣10","♣J","♣Q","♣K",
         "♦A","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦J","♦Q","♦K",
         "♠A","♠2","♠3","♠4","♠5","♠6","♠7","♠8","♠9","♠10","♠J","♠Q","♠K"]


while(True):
    hit_me = input("Do you want a card? y/n ")
    if (hit_me == "y"):
        card_number = random.randint(0,51)
        print ("Your card is "+cards[card_number])
    elif (hit_me == "n"):
        break
    else:
        print("Choose y or n to say if you want a card or not.")
