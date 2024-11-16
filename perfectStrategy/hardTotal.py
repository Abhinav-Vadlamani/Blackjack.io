import helper

hit = "hit"
stand = "stand"
double = "double"
surrender = "surrender"

def seventeen_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 17

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return stand

def sixteen_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 16

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if dealer up card is from 2-6, stand
    stand_set = {'2', '3', '4', '5', '6'}
    if dealer_value_card in stand_set:
        return stand
    
    # if dealer up card is 9, 10, face cards, or ace, surrender
    surrender_set = {'9', '10', 'Jack', 'Queen', 'King', 'Ace'}
    if dealer_value_card in stand_set:
        return surrender
    
    # else, hit
    else:
        return hit
    
def fifteen_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 15

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """
     
    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if dealer up card is from 2-6, stand
    stand_set = {'2', '3', '4', '5', '6'}
    if dealer_value_card in stand_set:
        return stand
    
    # if dealer up card is 10 or a face card, surrender
    surrender_set = {'10', 'Jack', 'Queen', 'King'}
    if dealer_value_card in surrender_set:
        return surrender
    
    # else, hit
    else:
        return hit
    
def fourteen_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 14

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """
     
    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if dealer up card is from 2-6, stand
    stand_set = {'2', '3', '4', '5', '6'}
    if dealer_value_card in stand_set:
        return stand
    
    # else, hit
    else:
        return hit
    
def thirteen_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 13

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """
     
    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if dealer up card is from 2-6, stand
    stand_set = {'2', '3', '4', '5', '6'}
    if dealer_value_card in stand_set:
        return stand
    
    # else, hit
    else:
        return hit
    
def twelve_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 12

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if card is from 4-6, stand
    stand_set = {'4', '5', '6'}
    if dealer_value_card in stand_set:
        return stand
    
    # else hit
    else:
        return hit
    
def eleven_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 11

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return double

def ten_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 10

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if dealer up card is a ten, face card, or ace, then hit
    hit_set = {'10', 'Jack', 'Queen', 'King', 'Ace'}
    if dealer_value_card in hit_set:
        return hit
    
    # else, double
    else:
        return double
    
def nine_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 9

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if dealer up is from 3-6, then double
    double_set = {'3', '4', '5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # else, hit
    else:
        return hit
    
def other_count(dealer_up_card: str):
    """
    returns what basic strategy says for player count 8 or less

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return hit