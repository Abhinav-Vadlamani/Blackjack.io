from perfectStrategy import hardTotal, softTotal, pairSplitting, helper

# pairSplitting dictionary for functions
pair_functions = {'2': pairSplitting.two_pair_splitting, '3': pairSplitting.three_pair_splitting, '4': pairSplitting.four_pair_splitting, 
         '5': pairSplitting.five_pair_splitting, '6': pairSplitting.six_pair_splitting, '7': pairSplitting.seven_pair_splitting,
         '8': pairSplitting.eight_pair_splitting, '9': pairSplitting.nine_pair_splitting, '10': pairSplitting.ten_face_pair_splitting,
         'Jack': pairSplitting.ten_face_pair_splitting, 'Queen': pairSplitting.ten_face_pair_splitting, 'King': pairSplitting.ten_face_pair_splitting,
         'Ace': pairSplitting.ace_pair_splitting}

# softTotal dictionary for functios
soft_total_functions = {'2': softTotal.ace_two, '3': softTotal.ace_three, '4': softTotal.ace_four, 
         '5': softTotal.ace_five, '6': softTotal.ace_six, '7': softTotal.ace_seven,
         '8': softTotal.ace_eight, '9': softTotal.ace_nine}

# hardTotal dictoinary for functions
hard_total_functions = {'17': hardTotal.seventeen_count, '16': hardTotal.sixteen_count, '15': hardTotal.fifteen_count, 
                        '14': hardTotal.fourteen_count, '13': hardTotal.thirteen_count, '12': hardTotal.twelve_count,
                        '11': hardTotal.eleven_count, '10': hardTotal.ten_count, '9': hardTotal.nine_count, 
                        '8': hardTotal.other_count, '7': hardTotal.other_count, '6': hardTotal.other_count,
                        '5': hardTotal.other_count, '4': hardTotal.other_count}

def basic_strategy(cards: set, dealer_up_card: str, value: int):
    """
    return what basic strategy says given a set of cards and the dealer up card

    Parameters:
    cards: a set of the players current cards
    dealer_up_card: a string of the current up card of the dealer
    value: an int representing the current player value
    """

    # return if set is a pair
    if helper.is_valid_pair(cards):
        pair_type = helper.return_pair_type(cards)
        output = pair_functions[pair_type](dealer_up_card)
        if output != "dont split":
            return pair_functions[pair_type](dealer_up_card)
    
    # return if set contains one ace for soft total
    if helper.is_valid_soft_total(cards):
        # compute total count for the cards besides the ace
        non_ace_count = 0
        for i in cards:
            if 'Ace' not in i:
                non_ace_count += int(helper.return_number_value(i))
        
        # return basic strategy
        return soft_total_functions[str(non_ace_count)](dealer_up_card)
    
    # else, return hardtotal
    return hard_total_functions[str(value)](dealer_up_card)

test = {'Ace of Hearts', '7 of Clubs'}
dealer = 'Ace of Clubs'
value = 20
print((basic_strategy(test, dealer,value)))