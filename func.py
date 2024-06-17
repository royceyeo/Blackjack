import random

def shuffle_card(cards):
    for card in cards:
        random.shuffle(cards[card])
        cards[card] = cards[card]
    return cards 

def check_suit(cards):
    deleted_suit = []
    updated_suit = []
    for suit in ["clubs", "diamonds", "hearts", "spades"]:
        if len(cards[suit]) == 0:
            deleted_suit.append(suit)
        else: pass
    for i in ["clubs", "diamonds", "hearts", "spades"]:
        if not i in deleted_suit: 
            updated_suit.append(i)
        else: pass
    return updated_suit

def pick_a_card(cards):
    suits = check_suit(cards)
    if len(suits) == 0:
        return "There is no more playing cards!"
    for suit in suits:
        if len(cards[suit]) == 0:
            del suits[suit]
    random_suit = random.choice(suits)
    random_card_index = random.randint(0, len(cards[random_suit]) -1)
    random_card = cards[random_suit][random_card_index]
    del cards[random_suit][random_card_index]
    return [[random_suit, random_card], [cards]]


def calculate_score(card_on_hand):
    score = convert_score(card_on_hand)
    total_score = calculate_sum(score)
    return total_score

def convert_score(card_on_hand): 
    score = []
    for index in range(0, len(card_on_hand), 1):
        score.append(card_on_hand[index][1])
    for index in range(0, len(score), 1):
        if score[index] == "King" or score[index] == "Queen" or score[index] == "Jack":
            score[index] = 10
        elif score[index] == "Ace":
            score[index] = 11
        else: pass
    return score

def calculate_sum(score):
    numA = 0
    for i in range(len(score)):
        if 11 == score[i]:
            numA +=1
    total_score = 0
    for i in score: 
        total_score += i
    if numA == 0: 
        return total_score
    else: 
        while total_score > 21 and numA > 0: 
            total_score -= 10
            numA -= 1
        return total_score

def get_card(player, cards): 
    take_card = pick_a_card(cards)
    player.append(take_card[0])
    cards = take_card[1][0]
    return [player, cards]

def sort_cards(cards):
    for things in cards:
        cards[things] = sort_mixed_list(cards[things])
    return cards
def sort_mixed_list(mixed_list):
    int_part = sorted([i for i in mixed_list if type(i) is int])
    str_part = sorted([i for i in mixed_list if type(i) is str])
    return int_part + str_part

def check_winner(player1, computer):
    player1_score = calculate_score(player1)
    computer_score = calculate_score(computer)
    if player1_score == computer_score:
        print(f"Draw! Player1 score is {player1_score} and computer score is {computer_score}")
        print(f"Holding cards of player 1 are {player1} and holding cards of computer are {computer}")
    elif len(computer) == 2 and computer[0][1] == "Ace" and computer[1][1] == "Ace" and player1 != computer:
        print(f"Blackjack: Computer Wins! Player1 score is {player1_score} and computer score is {computer_score}")
        print(f"Holding cards of player 1 are {player1} and holding cards of computer are {computer}")
    elif len(player1) == 2 and player1[0][1] == "Ace" and player1[1][1] == "Ace" and player1 != computer:
        print(f"Blackjack: Player1 Wins! Player1 score is {player1_score} and computer score is {computer_score}")
        print(f"Holding cards of player 1 are {player1} and holding cards of computer are {computer}")
    elif player1_score <= 21 and player1_score > computer_score or player1_score <= 21 and computer_score > 21:
        print(f"Player1 Wins! Player1 score is {player1_score} and computer score is {computer_score}")
        print(f"Holding cards of player 1 are {player1} and holding cards of computer are {computer}")
    elif computer_score <= 21 and computer_score > player1_score or computer_score <= 21 and player1_score > 21:
        print(f"Computer Wins! Player1 score is {player1_score} and computer score is {computer_score}")
        print(f"Holding cards of player 1 are {player1} and holding cards of computer are {computer}")
    else: 
        print(f"Both loss! Player1 score is {player1_score} and computer score is {computer_score}")
        print(f"Holding cards of player 1 are {player1} and holding cards of computer are {computer}")
