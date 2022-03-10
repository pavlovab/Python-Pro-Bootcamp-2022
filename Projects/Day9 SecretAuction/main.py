import art

print(art.logo)

import os
def clear(): 
    os.system('cls') 

secret_auction = {}
max_bid = 0
best_bidder = ""
more_bids = True

while more_bids:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    secret_auction[user_name] = user_bid
    if user_bid > max_bid:
        max_bid = user_bid
        best_bidder = user_name

    more_bids = input("Are there any more bids? 'Yes' or 'No': ").lower()
    clear()
    if more_bids == "no":
        more_bids = False
        print(f"The winner is {best_bidder} with a bid of ${secret_auction[best_bidder]}.")

