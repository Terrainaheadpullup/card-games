import random


def poker():
    # User inputs the amount they want to bet which is stored as int in the variable 'bet'
    money = input("Enter the amount you want to bet: ")
    bet = int(money)

    # Generates all the cards in the deck
    cards = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "1H", "JH", "QH", "KH",
             "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "1D", "JD", "QD", "KD",
             "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "1C", "JC", "QC", "KC",
             "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "1S", "JS", "QS", "KS"]

    # Chooses cards and removes cards chosen from the deck
    card_1 = random.choice(cards)
    cards.remove(card_1)

    card_2 = random.choice(cards)
    cards.remove(card_2)

    card_3 = random.choice(cards)
    cards.remove(card_3)

    card_4 = random.choice(cards)
    cards.remove(card_4)

    card_5 = random.choice(cards)
    cards.remove(card_5)

    # Splits the chosen cards into face and suit
    face_1 = card_1[0]
    suit_1 = card_1[1]

    face_2 = card_2[0]
    suit_2 = card_2[1]

    face_3 = card_3[0]
    suit_3 = card_3[1]

    face_4 = card_4[0]
    suit_4 = card_4[1]

    face_5 = card_5[0]
    suit_5 = card_5[1]

    # Puts the suits and faces into lists and sorts them to reduce the number of possible combinations for each
    # winning result
    suits = [suit_1, suit_2, suit_3, suit_4, suit_5]
    faces = [face_1, face_2, face_3, face_4, face_5]
    faces.sort()
    suits.sort()

    # Checks if your hand falls into a winning category
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4] and faces[0] == "1" and faces[1] == "A" and \
            faces[2] == "J" and faces[3] == "K" and faces[4] == "Q":
        print("Royal Flush")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 50, "points")

    elif suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        print("Flush")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 20, "points")

    elif faces[0] == faces[1] == faces[2] == faces[3] or faces[1] == faces[2] == faces[3] == faces[4]:
        print("Four of a Kind")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 12, "points")

    elif faces[0] == faces[1] == faces[2] and faces[3] == faces[4] or faces[0] == faces[1] and faces[2] == faces[3] == \
            faces[4]:
        print("Full House")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 8, "points")

    elif faces[0] == faces[1] == faces[2] or faces[1] == faces[2] == faces[3] or faces[2] == faces[3] == faces[4]:
        print("Three of a Kind")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 5, "points")

    elif faces[0] == faces[1] and faces[2] == faces[3] or faces[0] == faces[1] and faces[3] == faces[4] or faces[1] == \
            faces[2] and faces[3] == faces[4]:
        print("Two Pairs")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 2, "points")

    elif faces[0] == faces[1] or faces[1] == faces[2] or faces[2] == faces[3] or faces[3] == faces[4]:
        print("One Pair")
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won ", bet * 1, "points")

    else:
        print(card_1, card_2, card_3, card_4, card_5)
        print("You won 0 points")

    # Separates games to make it more readable
    print(" ")
    print("-----------------")
    print(" ")


def blackjack():
    # User inputs the amount they want to bet which is stored as int in the variable 'bet'
    money = input("Enter the amount you want to bet: ")
    bet = int(money)

    # Generates all the cards in the deck
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

    # Chooses cards and removes cards chosen from the deck
    card_1 = random.choice(cards)
    cards.remove(card_1)

    card_2 = random.choice(cards)
    cards.remove(card_2)

    card_3 = random.choice(cards)
    cards.remove(card_3)

    card_4 = random.choice(cards)
    cards.remove(card_4)

    your_total = int(card_1) + int(card_3)
    my_total = int(card_2) + int(card_4)

    print(card_1, card_3)

    # AI Twist
    if my_total < 12:
        card_6 = random.choice(cards)
        cards.remove(card_6)
        my_total += int(card_6)

    if 15 > my_total > 11:
        chance = random.random()
        if chance < 0.5:
            card_8 = random.choice(cards)
            cards.remove(card_8)
            my_total += int(card_8)

    if 19 > my_total > 16:
        chance_2 = random.random()
        if chance_2 < 0.15:
            card_10 = random.choice(cards)
            cards.remove(card_10)
            my_total += card_10

    # Allows you to twist up to 3 times
    for j in range(2, 5):
        stick_twist = input("stick or twist?: ")

        # Code if you twist
        if stick_twist == "twist":
            card_5 = random.choice(cards)
            cards.remove(card_5)
            your_total += int(card_5)
            if j == 2:
                card_7 = card_5
                print(card_1, card_3, card_7)
            elif j == 3:
                card_9 = card_5
                print(card_1, card_3, card_7, card_9)
            elif j == 4:
                card_11 = card_5
                print(card_1, card_3, card_7, card_9, card_11)

        # Breaks the for loop if you stick
        if stick_twist == "stick" or j == 4:
            break

    # Stuff that figures out who won
    if 21 > your_total < my_total < 21 or my_total < 21 < your_total:
        print("You lose! You got 0 points")
        print("You got.", your_total, "I got", my_total)

    elif 21 > my_total < your_total < 21 or my_total > 21 > your_total:
        print("You win! You got", bet * 2, "points")
        print("You got.", your_total, "I got", my_total)

    elif my_total == your_total or my_total > 21 and your_total > 21:
        print("It was a draw! You got", bet, "points")
        print("You got.", your_total, "I got", my_total)

    # Separates games to make it more readable
    print(" ")
    print("-----------------")
    print(" ")


while 1 == 1:
    game = input("Enter the name of the game. Enter cancel if you want to quit: ")
    if game == "poker":
        poker()
    elif game == "blackjack":
        blackjack()
    elif game == "cancel":
        break
