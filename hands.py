from enum import Enum

class Hand(Enum):
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH = 1

def same_suit(cards):
    suit = cards[0].suit
    for card in cards:
        if(card.suit is not suit):
            return False
    return True

def get_face_value(card, A_low = False):
    face = card.face
    if(A_low and face == 14):
        return 1
    return face


def in_sequence(cards, is_A_low = False):
    #is_A_high-- 2,3,4,5,6,7,8,9,10,J/11,Q/12,K/13,A/14
    #is_A_low-- A/1, 2,3,4,5,6,7,8,9,10,J/11,Q/12,K/13
    min_face = 15

    for card in cards:
        face = get_face_value(card, is_A_low)
        if(face < min_face):
            min_face = face
    
    visited = []
    for card in cards:
        face = get_face_value(card, is_A_low)
        visited[face - min_face] = face

    for face_value in visited:
        if face_value is 0:
            return False

    return len(visited) is 5

def can_make_sequence(cards):
    return (in_sequence(cards, is_A_low = False) or in_sequence(cards, is_A_low = True))


def get_frequencies(cards):
        #            2  3  4  5  6  7  8  9 10  J  Q  K  A
    freqs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in cards:
        freqs[card.face] = freqs[card.face] + 1
    return freqs

def is_royal_flush(cards):
    hasA = False
    hasK = False
    hasQ = False
    hasJ = False
    has10 = False
    
    for card in cards:
        if(card.face == 14):
            hasA = True
        if(card.face == 13):
            hasK = True
        if(card.face == 12):
            hasQ = True
        if(card.face == 11):
            hasJ = True
        if(card.face== 10):
            has10 = True
    
    return hasA and hasK and hasQ and hasJ and has10 and same_suit(cards)

def is_straight_flush(cards):
    return can_make_sequence(cards) and same_suit(cards)

def is_four_of_a_kind(cards):
    freqs = get_frequencies(cards)
    for freq in freqs:
        if freq is 4:
            return True
    return False

def is_full_house(cards):
    freqs = get_frequencies(cards)

    has_three_of_a_kind = False
    has_two_of_a_kind = False

    for freq in freqs:
        if freq is 3:
            has_three_of_a_kind = True
        if freq is 2:
            has_two_of_a_kind = True
            
    return has_three_of_a_kind and has_two_of_a_kind

def is_flush(cards):
    return same_suit(cards) and not can_make_sequence(cards)

def is_straight(cards):
    return can_make_sequence(cards) and not same_suit(cards)

def has_three_of_a_kind(cards):
    freqs = get_frequencies(cards)

    for freq in freqs:
        if freq is 3:
            return True
    return False

def has_two_pair(cards):
    num_pairs = 0
    freqs = get_frequencies(cards)

    for freq in freqs:
        if freq is 2:
            num_pairs = num_pairs + 1
    return num_pairs is 2
    
def has_pair(cards):
    freqs = get_frequencies(cards)

    for freq in freqs:
        if freq is 2:
            return True
    return False

def high_card(cards):
    max = 0
    for card in cards:
        if card.face > max:
            max = card.face

    return max

def get_hand(cards):
    if(is_royal_flush(cards)):
        return Hand.ROYAL_FLUSH
    if(is_straight_flush(cards)):
        return Hand.STRAIGHT_FLUSH
    if(is_four_of_a_kind(cards)):
        return Hand.FOUR_OF_A_KIND
    if(is_full_house(cards)):
        return Hand.FULL_HOUSE
    if(is_flush(cards)):
        return Hand.FLUSH
    if(is_straight(cards)):
        return Hand.STRAIGHT
    if(has_three_of_a_kind(cards)):
        return Hand.THREE_OF_A_KIND
    if(has_two_pair(cards)):
        return Hand.TWO_PAIR
    if(has_pair):
        return Hand.PAIR
    return Hand.HIGH

def score_hand(cards):
    score = 0
    for card in cards:
        score = score + card.face
    
    return score

def get_winning_hand(hands):
    hand_classifications = {
        Hand.ROYAL_FLUSH: [],
        Hand.STRAIGHT_FLUSH: [],
        Hand.FOUR_OF_A_KIND: [],
        Hand.FULL_HOUSE: [],
        Hand.FLUSH: [],
        Hand.STRAIGHT: [],
        Hand.THREE_OF_A_KIND: [],
        Hand.TWO_PAIR: [],
        Hand.PAIR: [],
        Hand.HIGH: []
    }
    highest_hand = Hand.HIGH

    for hand in hands:
        hand_classification = get_hand(hand.cards)
        if(hand_classification.value > highest_hand.value):
            highest_hand = hand_classification
        hand_classifications[hand_classification].append(hand)
    
    max_score = 0
    best_hand = None

    for tied_hand in hand_classifications[highest_hand]:
        score = score_hand(tied_hand.cards)
        if(score > max_score):
            max_score = score
            best_hand = tied_hand
    
    return best_hand