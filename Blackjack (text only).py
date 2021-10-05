import random
from itertools import product

# List of our accepted inputs. We can cut the list down by having python make every input upper or lower case for us.
yes = ['yes', 'Yes', 'yeah', 'Yeah', 'yup', 'Yup', 'y', 'Y', 'yea',
       'Yea', 'hit', 'Hit', 'HIT', 'h', 'H']
no = ['No', 'no', 'Nope', 'nope', 'N', 'n', 'Nah', 'nah', 'stay',
      'Stay', 'STAY', 'stick', 'Stick', 'STICK', 'S', 's']

line_space = ' '

# dictionary that takes the strings of each card and translates it to an integar that can be added together
def hand_values():
    global result_d, result_p
    card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "King": 10, "Queen": 10,
                  "Jack": 10, "Ace": 11}
    result_d = 0
    result_p = 0
    #Our integar values for dealer and player that is added to below

    #x.split(' ') needed to split the string so we can get exact matches. Otherwise the dictionary would be all 52 to possible combos
    for x in dealer_hand:
        result_d += card_value[x.split(' ')[0]]

        # Changes value of Ace to 1 if more then one Ace is in list or value exceeds 21. DEALER
        if "Ace" in x.split(' '):
            number_of_aces_d = x.split(' ').count("Ace")
            if number_of_aces_d > 2 or result_d > 21:
                result_d += -10


    for x in player_hand:
        result_p += card_value[x.split(' ')[0]]

        # Changes value of Ace to 1 if more then one Ace is in list or value exceeds 21. PLAYER
        if "Ace" in x.split(' '):
            number_of_aces_p = x.split(' ').count("Ace")
            if number_of_aces_p > 2 or result_p > 21:
                result_p += -10
                print("Total hand value over 21. One or more Aces now worth 1.")



# Loop to allow "play again?" part to work
def script_start():
    global dealer_hand, player_hand

    # Asks the player if they want to play again then returns to start or exits.
    def play_again():
        print(line_space)
        again_question = input("Do you want to play again? ")
        if again_question in yes:
            script_start()
        elif again_question in no:
            print(line_space)
            print("Come back soon!")
            exit()
        else:
            print("Unknown command")
            play_again()

    # All integar values of hands are checked here to see who wins.
    def hand_condition_results():
        global dealer_hand, player_hand
        if (result_d) == 21 and (result_p) == 21:
            print("Dealer and player have Blackjack. PUSH.")
            play_again()
        elif (result_d == 21) and (result_p !=21):
            print("Dealer has Blackjack! House wins!")
            play_again()
        elif (result_d != 21) and (result_p ==21):
            print("Player has Blackjack! You win!")
            play_again()
        elif (result_d > 21) and (result_p < 21):
            print("Dealer BUST! You win!")
            play_again()
        elif (result_d < 21) and (result_p > 21): #player bust condition might move to append
            print("You are BUST! House wins.")
            play_again()
        elif (result_d > 21) and (result_p > 21):
            print("Both are bust!")
        elif (result_d < 21) and (result_p < 21):
            if result_d > result_p:
                print("Dealer is closer to 21. House Wins")
                play_again()
            elif result_d < result_p:
                print("You are closer to 21. YOU WIN!")
                play_again()
            elif result_d == result_p:
                print("Both players are equal and under 21. PUSH.")
                play_again()
        else:
            print("Error in results")


    #Deck creation, deck shuffle and first two cards of player and dealer.
    dealer_hand = []
    player_hand = []

    card_face = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen", "Jack", "Ace"]
    card_suit = ["Diamonds", "Spades", "Clubs", "Hearts"]

    # product creates one of every suit for each number/card face. IMPORTED FROM ITERTOOLS
    deck = ["%s of %s"%(x, y) for x, y in product(card_face, card_suit)]

    random.shuffle(deck)
    #print(deck)
    # Show deck for testing/cheating

    #Dealer and Player are given first two cards from deck list then the cards are deleted from the deck list.
    dealer_hand = deck[:2]
    for _ in range(2): deck.pop(0)
    print(line_space)
    print("Dealer has a face down and", dealer_hand[1])
    print(line_space)
    # doesn't require a space on the end of the string for some reason

    player_hand = deck[:2]
    for _ in range(2): deck.pop(0)
    print("Player has", player_hand[0], "and", player_hand[1])
    hand_values()
    print("Totaling", result_p)
    print(line_space)

    # In blackjack the dealer gives themselves cards until they have a value of 17 or higher. Then go to results.
    def add_to_dealer_hand():
        global dealer_hand
        print("Dealer reveals there face down to be", dealer_hand[0])
        print("Dealer has", dealer_hand)
        print("Totaling", result_d)
        #time.sleep(2.5) # pause script so player can read text
        print(line_space)
        while result_d <= 16: #16 instead of 17 because this is a greater than or EQUAL TO, "< 17" broke the script when the dealer got 17.
            dealer_hand += deck[:1]
            deck.pop(0)
            print("Dealer hits. Now has ", dealer_hand)
            hand_values()
            print("Totaling ", result_d)
            print(line_space)
        hand_condition_results()

    # Player is given cards or passes to dealer based on their input. Accepted inputs come from lists above.
    while result_p < 21:
        question_player = input("Hit? ")
        if question_player.lower() in yes: #adding .lower on to our input response forces the case sensitvity to be lower. upper for upper
            player_hand += deck[:1]
            deck.pop(0)
            print("Now have ", player_hand)
            hand_values()
            print("Totaling ", result_p)
        elif question_player in no:
            break
    print(line_space)
    print("Now the dealer.")
    #time.sleep(2.5) #pauses script so player can read.
    print(line_space)
    add_to_dealer_hand()

#Start loop
script_start()


# get ACES working. Done! Then use as core for GUI version