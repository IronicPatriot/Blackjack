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
    global dealer_hand, print_num
    card_image = ImageTk.PhotoImage(Image.open(deck[0]).resize((180, 245), Image.ANTIALIAS))
    card_label = Label(dealer_frame, image=card_image, relief="raised")
    card_label.image = card_image
    card_label.pack(side="left")
    dealer_hand.append(deck.pop(0))
    #print(dealer_hand)

    #split strings in hand to find integars using card_value dictionary
    print_num = 0
    for x in dealer_hand: #without the zero it gives 380
        print_num += card_value[x.split('-')[0]]

        if "images/ace" in x.split('-'):
            number_of_aces_d = x.split('-').count("images/ace")
            if number_of_aces_d > 2 or print_num > 21:
                print_num += -10
                #print("Total hand value over 21. One or more Aces now worth 1 for dealer.")

    dealer_label = Label(dealer_score, text="Dealer").grid(column=0,row=0)
    num_label = Label(dealer_score, text=print_num).grid(column=0,row=1)

deal_dealer()
deal_dealer()

# player hand
def deal_player():
    global player_hand, print_num2
    card_image = ImageTk.PhotoImage(Image.open(deck[0]).resize((180, 245), Image.ANTIALIAS))
    card_label = Label(player_frame, image=card_image, relief="raised")
    card_label.image = card_image
    card_label.pack(side="left")
    player_hand.append(deck.pop(0))
    #print(player_hand)

    print_num2 = 0
    for x in player_hand: #without the zero it gives 380
        print_num2 += card_value[x.split('-')[0]]

        if "images/ace" in x.split('-'):
            number_of_aces_p = x.split('-').count("images/ace")
            if number_of_aces_p > 2 or print_num2 > 21:
                print_num2 += -10
                #print("Total hand value over 21. One or more Aces now worth 1 for player")

    player_label = Label(player_score, text="Player").grid(column=0, row=0)
    num_label = Label(player_score, text=print_num2).grid(column=0,row=1)
deal_player()
deal_player()
#print(print_num2)

def check_winner():
    global print_num, print_num2
    if (print_num) == 21 and (print_num2) == 21:
        Label(root, text="Dealer and player have Blackjack. DRAW.", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (print_num == 21) and (print_num2 != 21):
        Label(root, text="Dealer has Blackjack! House wins!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (print_num != 21) and (print_num2 == 21):
        Label(root, text="Player has Blackjack! You win!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (print_num > 21) and (print_num2 < 21):
        Label(root, text="Dealer BUST! You win!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (print_num < 21) and (print_num2 > 21):  # player bust condition might move to append
        Label(root, text="Dealer Wins!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (print_num > 21) and (print_num2 > 21):
        Label(root, text="Both are bust!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    elif (print_num < 21) and (print_num2 < 21):
        if print_num > print_num2:
            Label(root, text="Dealer is closer to 21. House Wins", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
        elif print_num < print_num2:
            Label(root, text="You are closer to 21. YOU WIN!", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
        elif print_num == print_num2:
            Label(root, text="Both players are equal and under 21. DRAW.", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)
    else:
        Label(root, text="Error in results.", font=('Helvetica', 45, 'bold')).grid(row=3, column=1)

def stay():
    hit_button.config(state=DISABLED)
    while print_num <= 16:
        deal_dealer()
    check_winner()

def player_hit():
    if print_num2 < 21:
        deal_player()
        #print(print_num2)
        if print_num2 >=21:
            stay()
    else:
        stay()

def new_game():
    global print_num, print_num2, dealer_hand, player_hand, deck
    print_num = 0
    num_label = Label(dealer_score, text=print_num).grid(column=0, row=1)
    dealer_frame.destroy()
    print_num2 = 0
    num_label = Label(player_score, text=print_num2).grid(column=0, row=1)
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

    deal_dealer()
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
