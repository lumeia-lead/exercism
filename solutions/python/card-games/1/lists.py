"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    result = []
    for i in range (3):
        result.append(number)
        number += 1
    return result


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    for num in rounds:
        if num == number:
            return True
    return False



def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    sum_cards = 0
    count_cards = 0
    for card in hand:
        sum_cards += card
        count_cards += 1
        average = sum_cards/count_cards
    return average


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    last_digit_index = len(hand) - 1
    last_digit = hand[last_digit_index]
    first_digit = hand[0]
    approx_average = (last_digit + first_digit) / 2
    true_average = card_average(hand)
    middle_card_index = int(len(hand)/2)
    middle_card = hand[middle_card_index]
    if (true_average == approx_average) or (true_average == middle_card):
        return True
    else: return False
        
        
        


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even = hand[::2]
    odd = hand[1::2]
    odd_sum = 0
    odd_count = 0
    even_sum = 0
    even_count = 0

    for odd_num in odd:
        odd_sum += odd_num
        odd_count += 1
    for even_num in even:
        even_sum += even_num
        even_count += 1
        
    odd_indices_average = odd_sum/odd_count
    even_indices_average = even_sum/even_count

    return odd_indices_average == even_indices_average


    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    last_index = len(hand) - 1
    last_card = hand[last_index]
    if last_card == 11:
        hand[last_index] = last_card*2
    return hand
