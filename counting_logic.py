import random

# Creating set of cards
ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'}
suits = {'Hearts', 'Diamonds', 'Clubs', 'Spades'}
deck_of_cards = {f"{rank} of {suit}" for rank in ranks for suit in suits}

# Tally of current cound of cards
count = 0

# Sets of cards based on count
positive_count = {'2', '3', '4', '5', '6'}
neutral_count = {'7', '8', '9'}
negative_count = {'10', 'Jack', 'Queen', 'King'}
positive_count_cards = {f"{rank} of {suit}" for rank in positive_count for suit in suits}
neutral_count_cards = {f"{rank} of {suit}" for rank in neutral_count for suit in suits}
negative_count_cards = {f"{rank} of {suit}" for rank in negative_count for suit in suits}

# set of cards already dealt
dealt_cards = set()

# Dictionary of numerical value of each card
# Ace value is 1 or 11, logic will be executed later
card_values = {}
for card in deck_of_cards:
    rank = card.split(" ")[0]
    if rank.isdigit():
        card_values[card] = int(rank)
    elif rank in ["Jack", "Queen", "King"]:
        card_values[card] = 10
    else:
        print(card)

# helper function to update count
def update_count(card):
    global count
    if card in positive_count_cards:
        count += 1
    elif card in negative_count_cards:
        count -= 1

def deal():
    # Deal the first card
    curr_card = random.choice(list(deck_of_cards))
    # Update count
    update_count(curr_card)
    # Add cards to dealt cards
    deck_of_cards.remove(curr_card)
    dealt_cards.add(curr_card)
    return curr_card

def start_play():
    # Player first card
    player_first_card = deal()
    # Dealer first card
    dealer_second_card = deal()
    # Player second card
    player_second_card = deal()
    # Dealer second card
    dealer_second_card = deal()
    
    return (player_first_card, dealer_second_card, player_second_card, dealer_second_card)

# play two rounds
for i in range(2):
    (player_first_card, dealer_first_card, player_second_card, dealer_second_card) = start_play()

    # Make sets for Ace total sum logic
    player_cards = set()
    dealer_cards = set()
    player_cards.add(player_first_card); player_cards.add(player_second_card)
    dealer_cards.add(dealer_first_card); dealer_cards.add(dealer_second_card)
    
    player_value = card_values[player_first_card] + card_values[player_second_card]

    # Give player information
    print(f"Dealer first card: {dealer_first_card}")
    print(f"Your first card: {player_first_card}")
    print(f"Your second card: {player_second_card}")

    # Player hit logic
    bust = False
    player_hit = True
    while player_hit:
        hit_or_not = input("Would you like to hit (Yes or No): ")
        # If player wants to hit, deal card and check card value
        if hit_or_not == "Yes":
            # Deal card and add card to player set, update player value
            hit_card = deal()
            print(f"Hit Card: {hit_card}")
            player_cards.add(hit_card)
            player_value += card_values[hit_card]

            # Check if player busts
            if player_value > 21:
                print("You Bust!")
                player_hit = False
                bust = True
            
            if player_value == 21:
                print("You Win!")
                player_hit = False
        # If player doesn't want to hit, break out of the loop
        else:
            player_hit = False

    # If player busts, move on to next round
    if bust:
        print(count)
        continue

    # Run through dealer play
    print(f"Dealer second card: {dealer_second_card}")
    dealer_value = card_values[dealer_first_card] + card_values[dealer_second_card]
    while dealer_value < 17: 
        dealer_hit_card = deal()
        print(f"Dealer hit card: {dealer_hit_card}")
        dealer_value += card_values[dealer_hit_card]
    
    # Check conditions for if player wins or not
    if dealer_value == 21:
        print("You Lost!")
    elif dealer_value > 21:
        print("You Win!")
    elif dealer_value >= player_value:
        print("You Lost!")
    else:
        print("You Win!")
    

            




