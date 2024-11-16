# This file focuses on pair splitting basic strategy
import helper

split = "split"
dont_split = "dont split"

def ace_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for ace pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return split

def ten_face_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for ten pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return dont_split

def nine_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for nine pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if 2-6 or 8-9, return split
    split_set = {'2', '3', '4', '5', '6', '8', '9'}
    if dealer_value_card in split_set:
        return split
    
    # else, don't split
    else:
        return dont_split
    
def eight_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for eight pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return split

def seven_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for seven pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if 2-7, return split
    split_set = {'2', '3', '4', '5', '6', '7'}
    if dealer_value_card in split_set:
        return split
    
    # else, don't split
    else:
        return dont_split
    
def six_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for seven pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if 2-6, return split
    split_set = {'2', '3', '4', '5', '6'}
    if dealer_value_card in split_set:
        return split
    
    # else, don't split
    else:
        return dont_split

def five_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for seven pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return dont_split

def four_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for four pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    return dont_split

def three_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for three pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if 4-7, return split
    split_set = {'4', '5', '6', '7'}
    if dealer_value_card in split_set:
        return split
    
    # else, don't split
    else:
        return dont_split
    
def two_pair_splitting(dealer_up_card: str):
    """
    returns what basic strategy says for three pair

    Parameters:
    dealer_up_card: a string of the current up card of the dealer
    """

    dealer_value_card = helper.return_number_value(dealer_up_card)

    # if 4-7, return split
    split_set = {'4', '5', '6', '7'}
    if dealer_value_card in split_set:
        return split
    
    # else, don't split
    else:
        return dont_split