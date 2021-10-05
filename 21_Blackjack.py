from tkinter import *
from PIL import ImageTk, Image
import random

root =Tk()
root.title('21 Blackjack')
root.iconbitmap('images/21_cards.ico')
root.geometry('1280x750')
root.configure(bg='green')

#deck building
suits = ['hearts', 'clubs', 'diamonds', 'spades']
face_cards = ['ace', 'jack', 'queen', 'king']
deck = []
extension = 'png'

hidden_card_name = []
hidden_card_value = []

for y in suits:
    for x in range(2, 11):
        name = 'images/{}-{}.{}'.format(str(x), y, extension)
        deck.append(name)

    for x in face_cards:
        name = 'images/{}-{}.{}'.format(str(x), y, extension)
        deck.append(name)
random.shuffle(deck)
# print(deck)

#card value for displaying integar of hand values
card_value = {"images/2": 2, "images/3": 3, "images/4": 4, "images/5": 5, "images/6": 6, "images/7": 7, "images/8": 8,
              "images/9": 9, "images/10": 10, "images/king": 10, "images/queen": 10, "images/jack": 10, "images/ace": 11}

dealer_hand = []
player_hand = []

#frames
def frames():
    global dealer_score, dealer_frame, player_score, player_frame
    dealer_frame = LabelFrame(root, bg='green')
    dealer_frame.grid(row=0, column=1, sticky="nsew")
    dealer_score = LabelFrame(root,  padx=30, pady=100, bg='black')
    dealer_score.grid(row=0, column=0)
    player_frame = LabelFrame(root, bg='green')
    player_frame.grid(row=1, column=1, sticky="nsew")
    player_score = LabelFrame(root,  padx=30, pady=100, bg='black')
    player_score.grid(row=1, column=0)
frames()

# add card dealer
def deal_dealer():
    global dealer_hand, dealer_num
    card_image = ImageTk.PhotoImage(Image.open(deck[0]).resize((180, 245), Image.ANTIALIAS))
    card_label = Label(dealer_frame, image=card_image, relief="raised")
    card_label.image = card_image
    card_label.pack(side="left")
    dealer_hand.append(deck.pop(0))
    # print(dealer_hand)

    # split strings in hand to find integars using card_value dictionary
    dealer_num = 0
    for x in dealer_hand:
        dealer_num += card_value[x.split('-')[0]]

        if "images/ace" in x.split('-'):
            number_of_aces_d = x.split('-').count("images/ace")
            if number_of_aces_d > 2 or dealer_num > 21:
                dealer_num += -10
                # print("Total hand value over 21. One or more Aces now worth 1 for dealer.")

    if len(dealer_hand) == 2:
        dealer_num = dealer_num - hidden_num
    '''disabled hidden value for testing'''


    print("new card total ", dealer_num)
    dealer_label = Label(dealer_score, text="Dealer:").grid(column=0,row=0)
    num_label = Label(dealer_score, text=dealer_num).grid(column=0,row=1)


def hidden_dealer():
    global dealer_hand, hidden_label, hidden_card_name, hidden_num
    card_image = ImageTk.PhotoImage(Image.open(deck[0]).resize((180, 245), Image.ANTIALIAS))
    hidden_label = Label(dealer_frame, image=card_image, relief="raised")
    hidden_label.image = card_image
    hidden_label.pack(side="left")
    hidden_card_name = deck[0]
    print(hidden_card_name)
    dealer_hand.append(deck.pop(0))
    # print(dealer_hand)

    # split strings in hand to find integars using card_value dictionary
    hidden_num = 0
    for x in dealer_hand:
        hidden_num += card_value[x.split('-')[0]]

        if "images/ace" in x.split('-'):
            number_of_aces_d = x.split('-').count("images/ace")
            if number_of_aces_d > 2 or hidden_num > 21:
                hidden_num += -10
                # print("Total hand value over 21. One or more Aces now worth 1 for dealer.")

    print("hidden ", hidden_num)

    card_art = ImageTk.PhotoImage(Image.open("images/card-back.png").resize((180, 245), Image.ANTIALIAS))
    hidden_label.configure(image=card_art)
    hidden_label.image = card_art

def reveal_card():
    global dealer_num
    num_label = Label(dealer_score, text=dealer_num).grid(column=0, row=1)
    print("reveal ", dealer_num)
    card_art = ImageTk.PhotoImage(Image.open(hidden_card_name).resize((180, 245), Image.ANTIALIAS))
    hidden_label.configure(image=card_art)
    hidden_label.image = card_art

hidden_dealer()
deal_dealer()

# player hand
def deal_player():
    global player_hand, player_num
    card_image = ImageTk.PhotoImage(Image.open(deck[0]).resize((180, 245), Image.ANTIALIAS))
    player_label = Label(player_frame, image=card_image, relief="raised")
    player_label.image = card_image
    player_label.pack(side="left")
    player_hand.append(deck.pop(0))
    # print(player_hand)

    player_num = 0
    for x in player_hand: #without the zero it gives 380
        player_num += card_value[x.split('-')[0]]

        if "images/ace" in x.split('-'):
            number_of_aces_p = x.split('-').count("images/ace")
            if number_of_aces_p > 2 or player_num > 21:
                player_num += -10
                # print("Total hand value over 21. One or more Aces now worth 1 for player")

    player_label = Label(player_score, text="Player:").grid(column=0, row=0)
    num_label = Label(player_score, text=player_num).grid(column=0,row=1)


deal_player()
deal_player()
#print(player_num)

def check_winner():
    global dealer_num, player_num
    if (dealer_num) == 21 and (player_num) == 21:
        Label(root, text="Dealer and player have Blackjack. DRAW.", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (dealer_num == 21) and (player_num != 21):
        Label(root, text="Dealer has Blackjack! House wins!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (dealer_num != 21) and (player_num == 21):
        Label(root, text="Player has Blackjack! You win!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (dealer_num > 21) and (player_num < 21):
        Label(root, text="Dealer BUST! You win!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (dealer_num < 21) and (player_num > 21):  # player bust condition might move to append
        Label(root, text="Dealer Wins!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (dealer_num > 21) and (player_num > 21):
        Label(root, text="Both are bust!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (dealer_num < 21) and (player_num < 21):
        if dealer_num > player_num:
            Label(root, text="Dealer is closer to 21. House Wins", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
        elif dealer_num < player_num:
            Label(root, text="You are closer to 21. YOU WIN!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
        elif dealer_num == player_num:
            Label(root, text="Both players are equal and under 21. DRAW.", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    else:
        Label(root, text="Error in results.", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)

def stay():
    reveal_card()
    hit_button.config(state=DISABLED)
    while dealer_num <= 16:
        deal_dealer()
    check_winner()

def player_hit():
    if player_num < 21:
        deal_player()
        #print(player_num)
        if player_num >=21:
            stay()
    else:
        stay()

def new_game():
    global dealer_num, player_num, dealer_hand, player_hand, deck, hidden_num
    dealer_num = 0
    hidden_num = 0
    num_label = Label(dealer_score, text=dealer_num).grid(column=0, row=1)
    dealer_frame.destroy()
    player_num = 0
    num_label = Label(player_score, text=player_num).grid(column=0, row=1)
    player_frame.destroy()
    hit_button.config(state=NORMAL)
    for label in root.grid_slaves():
        if int(label.grid_info()["row"]) == 3:
            label.destroy()

    frames()

    dealer_hand.clear()
    player_hand.clear()
    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    face_cards = ['ace', 'jack', 'queen', 'king']
    deck = []
    extension = 'png'

    for y in suits:
        for x in range(2, 11):
            name = 'images/{}-{}.{}'.format(str(x), y, extension)
            deck.append(name)

        for x in face_cards:
            name = 'images/{}-{}.{}'.format(str(x), y, extension)
            deck.append(name)
    random.shuffle(deck)

    hidden_dealer()
    deal_dealer()

    deal_player()
    deal_player()
    #print(deck)

# Buttons
buttons_frame = LabelFrame(root, bg="green")
buttons_frame.grid(row=2, column=1, sticky="nsew")
hit_button = Button(buttons_frame, text="Hit", padx=30, pady=30, command=player_hit)
hit_button.grid(row=2, column=1) # has to be on separate line otherwise disabling doesn't work
stay_button = Button(buttons_frame, text="Stay", padx=30, pady=30, command=stay).grid(row=2, column=2)
new_button = Button(buttons_frame, text="New Game", padx=30, pady=30, command=new_game).grid(row=2, column=3)


root.mainloop()
