clear = lambda: os.system('cls')
import blackjack_art as art

print(art.logo)
cards = {
"clubs": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack"],
"diamonds": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack"],
"hearts": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack"],
"spades": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack"],
}
cards = func.shuffle_card(cards)

player1 = []
computer = []

# Start Game: Issue two cards to each player. 
for i in range(2): 
    result = func.get_card(player1, cards)
    player1 = result[0]
    result = func.get_card(computer, cards)
    computer = result[0]
cards = result[1]
print(player1)

should_continue = True
while should_continue:
    want_card = input(f"Do you want to get another card? Current Total score is {func.calculate_score(player1)}. Type 'no' to end.\n").lower()
    if want_card == "no": 
        should_continue = False
    else: 
        result = func.get_card(player1, cards)
        player1 = result[0]
        cards = result[1]
        print(player1)

should_continue = True
while should_continue:
    if func.calculate_score(computer) > 16: 
        should_continue = False
    else: 
        result = func.get_card(computer, cards)
        computer = result[0]
        cards = result[1]

clear()
func.check_winner(player1, computer)
