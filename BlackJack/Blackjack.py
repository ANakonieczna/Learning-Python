import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal(cards):
    return random.choice(cards)


def bj_game():
    comp_cards = []
    my_cards = []
    my_cards.append(deal(cards))

    still_play = "y"

    while still_play == "y":
        if sum(comp_cards) <= 17:
            card = deal(cards)
            if card == 11 and sum(comp_cards) + card > 21:
                card = 1
            comp_cards.append(card)
        card = deal(cards)
        if card == 11 and sum(my_cards) + card > 21:
            card = 1
        my_cards.append(card)

        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {comp_cards[0]}")

        if sum(my_cards) < 21:
            still_play = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
        else:
            still_play = "n"

    print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
    print(
        f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")

    if sum(my_cards) <= 21:
        if sum(comp_cards) > 21:
            print("You win.")
        else:
            if sum(my_cards) > sum(comp_cards):
                print("You win.")
            elif sum(my_cards) < sum(comp_cards):
                print("Computer wins.")
            else:
                print("It's a draw.")
    elif sum(comp_cards) <= 21:
        print("Computer wins.")
    else:
        print("It's a draw.")

    if input("Do you want to play the game of Blackjack? Type 'y' or 'n': "
             ).lower() == "y":
        clear()
        print(logo)
        bj_game()


print(logo)
bj_game()
