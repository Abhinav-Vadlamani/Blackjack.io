def return_number_value(card: str):
    """
    Given a card, return the numeric value of it

    Parameters:
    card: a string of the card
    """
    
    str_split_array = str.split(" ")

    # return desired element
    # can't return number because of 
    return str_split_array[0]

def is_valid_pair(cards: set):
    """
    Given a set of cards, returns if it can be split or not

    Parameters:
    cards: a string set of the current cards that a player has
    """
    if len(cards) != 2:
        return False
    
    # to eliminate concurrent modification
    is_valid_pair_set = set(cards)

    # compare cards
    card1 = is_valid_pair_set.pop()
    card2 = is_valid_pair_set.pop()

    card1_value = return_number_value(card1)
    card2_value = return_number_value(card2)

    return card1_value == card2_value

def return_pair_type(cards: set):
    """
    Given a pair, return what the numeric type of the pair is

    Parameters:
    cards: a string set of the current cards that a player has
    """

    temp_set = set(cards)

    card1_value = temp_set.pop()
    return return_number_value(card1_value)

def is_valid_soft_total(cards: set):
    """
    Given a set of player cards, determine if it applies to the soft total category of
    """

    # retrieve the total number of aces
    aces = 0
    for card in cards:
        if "Ace" in card:
            aces += 1
    
    if aces != 1:
        return False
    
    else:
        return True
    