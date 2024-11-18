from .helper import *

hit = "hit"
stand = "stand"
double = "double"

def ace_nine(dealer_up_card: str):
    """
    returns what basic strategy says for ace-nine pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """
    
    return stand

def ace_eight(dealer_up_card: str):
    """
    returns what basic strategy says for ace-eight pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is 6, then double
    if dealer_value_card == "6":
        return double
    else:
        return stand

def ace_seven(dealer_up_card: str):
    """
    returns what basic strategy says for ace-seven pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is from 2-6, then double
    double_set = {'2', '3', '4', '5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # if dealer up card is from 7-8, then stand
    stand_set = {'7', '8'}
    if dealer_value_card in stand_set:
        return stand
    
    # else, hit
    else:
        return hit
    
def ace_six(dealer_up_card: str):
    """
    returns what basic strategy says for ace-six pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is from 3-6, then double
    double_set = {'3', '4', '5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # else, hit
    else:
        return hit

def ace_five(dealer_up_card: str):
    """
    returns what basic strategy says for ace-five pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is from 4-6, then double
    double_set = {'4', '5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # else, hit
    else:
        return hit
    
def ace_four(dealer_up_card: str):
    """
    returns what basic strategy says for ace-four pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is from 4-6, then double
    double_set = {'4', '5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # else, hit
    else:
        return hit
    
def ace_three(dealer_up_card: str):
    """
    returns what basic strategy says for ace-three pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is from 5-6, then double
    double_set = {'5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # else, hit
    else:
        return hit

def ace_two(dealer_up_card: str):
    """
    returns what basic strategy says for ace-two pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = return_number_value(dealer_up_card)

    # if dealer up card is from 5-6, then double
    double_set = {'5', '6'}
    if dealer_value_card in double_set:
        return double
    
    # else, hit
    else:
        return hit
    