'''This module contains all the necessary functions for the Blackjack gameplay'''



def card_name(card_rank):
    '''Used to get the name of a card when given the rank
    Args:
        Takes in the card rank (integer)
    Returns:
        Card name of a particular rank
    Examples:
        card_name(1) == "Ace"
        card_name(2) == "2"
        card_name(3) == "3"
    '''
    if card_rank == 1:
        name = "Ace"
    elif card_rank < 11:
        name = str(card_rank)
    elif card_rank == 11:
        name = "Jack"
    elif card_rank == 12:
        name = "Queen"
    else:
        name = "King"
    return name


def card_value(card_rank):
    '''Returns the card value of a given card rank integer.
    Args:
        Card rank integer.
    Returns:
        Card numerical value.
    Examples:
        card_value(1) == 11
        card_value(2) == 2
        card_value(3) == 3
        card_value(4) == 4
        card_value(5) == 5.
    '''
    if card_rank == 1:
        value = 11
    elif card_rank < 11:
        value = card_rank
    else:
        value = 10
    return value


def end_turn_status(hand):
    '''This function returns the game status of the user or dealer based on current hand value
    Args:
        Takes in the current hand value of the dealer or user.
    Returns:
        Returns "BLACKJACK!", "BUST.", or nothing depending on the hand value entered
    Examples:
        assert end_turn_status(21) == "BLACKJACK!"
        assert end_turn_status(24) == "BUST."
        assert end_turn_status(18) == ""
    '''
    if hand == 21:
        return'BLACKJACK!'
    elif hand > 21:
        return "BUST."
    else:
        return ""


def end_game_status(user_hand, dealer_hand):
    '''This function determines who is the winner between the user and the dealer.
    Args:
        It takes in the final hand value of the user and the dealer.
    Returns:
        It returns 'You win!' or 'Dealer wins!." or "Tie".
    Examples:
        assert end_game_status(18,18) == "Tie."
        assert end_game_status(18,17) == "You win!"
        assert end_game_status(17,19) == "Dealer wins!"
        assert end_game_status(18,21) == "Dealer wins!"
        assert end_game_status(21,18) == "You win!"
    '''
    if (user_hand > dealer_hand) and user_hand < 21:
        status = "You win!"
    elif (dealer_hand > user_hand) and dealer_hand < 21:
        status = "Dealer wins!"
    elif user_hand == 21 and dealer_hand != 21:
        status = "You win!"
    elif dealer_hand == 21 and user_hand != 21:
        status = "Dealer wins!"
    elif dealer_hand < 21 and user_hand < 21:
        if dealer_hand == user_hand:
            status = "Tie."
        elif dealer_hand < user_hand:
            status = "Dealer Wins!"
        else:
            status = "You win!"
    elif dealer_hand < 21 and user_hand > 21:
        status = "Dealer Wins!"
    elif user_hand < 21  and dealer_hand > 21:
        status = "You win!"
    else:
        status = "Tie."
    return status