# GUI version of Blackjack script

from tkinter import *
from PIL import ImageTk, Image
import random
from random import randint
from itertools import product

root =Tk()
root.title('22 Blackjack')
root.iconbitmap('images/21_cards.ico')
root.geometry('1280x750')
root.configure(bg='green')

dealer_hand = []
player_hand = []

###### Plan/notes ######
#Its not going to print to the terminal, so deck doesn't need to print "of", just number and clubs giving us our file names to!
#Use grid to have cards print to right of the last one in their respective hands/sections
#Resize cards smaller (add button to make them larger?)
#Make cards relief=sunken for style
#assign image to card when deck is created

#deck building
card_face = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "king", "queen", "jack", "ace"]
card_suit = ["diamonds", "spades", "clubs", "hearts"]

deck = ["%s-%s"%(x, y) for x, y in product(card_face, card_suit)]
random.shuffle(deck)

#card value for displaying integar of hand values
card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "king": 10, "queen": 10,
                  "jack": 10, "ace": 11}

#first dealer card
dealer_hand = deck[:2]
for _ in range(2): deck.pop(0)

#left and right frames
dealer_frame = LabelFrame(root, bg='green')
dealer_frame.pack(fill='both', side='left', expand='True')
player_frame = LabelFrame(root, bg='green')
player_frame.pack(fill='both', side='right', expand='True')
deck_frame = LabelFrame(root, bg='green')
deck_frame.pack(fill='both', side='bottom', expand='true')
bottom = Label(deck_frame, text="deck test here").pack()

#image name assigment and print
temp = dealer_hand[0]
image_pick = 'images/' + temp + '.png'
print_image = ImageTk.PhotoImage(Image.open(image_pick).resize((180, 245), Image.ANTIALIAS)) # image antialias isn't required but looks better with it
image_label = Label(dealer_frame, image=print_image).grid(row=0, column=0)
image_pick_2 = 'images/' + dealer_hand[1] + '.png'
print_image_2 = ImageTk.PhotoImage(Image.open(image_pick_2).resize((180, 245), Image.ANTIALIAS))
image_label_2 = Label(dealer_frame, image=print_image_2).grid(row=0, column=1)

#split strings in hand to find integars using card_value dictionary
print_num = 0
for x in dealer_hand: #without the zero it gives 380
    print_num += card_value[x.split('-')[0]]

num_label = Label(dealer_frame, text=print_num).grid(row=1, column=0)
#################### player stuff below (right side) ####################

# player hand
player_hand = deck[:2]
for _ in range(2): deck.pop(0)

image_pick_p = 'images/' + player_hand[0] + '.png' #can't just link to first image pick, doesn't refresh deck list when we call it again
print_image_p = ImageTk.PhotoImage(Image.open(image_pick_p).resize((180, 245), Image.ANTIALIAS))
image_label_p = Label(player_frame, image=print_image_p).grid(row=0, column=0)
image_pick_2p = 'images/' + player_hand[1] + '.png'
print_image_2p = ImageTk.PhotoImage(Image.open(image_pick_2p).resize((180, 245), Image.ANTIALIAS))
image_label_2p = Label(player_frame, image=print_image_2p).grid(row=0, column=1)


print_num2 = 0
for x in player_hand: #without the zero it gives 380
    print_num2 += card_value[x.split('-')[0]]

num_label = Label(player_frame, text=print_num2).grid(row=1, column=0)

deck_image = 'images/' + deck[0] + '.png'
deck_print = ImageTk.PhotoImage(Image.open(deck_image).resize((180, 245), Image.ANTIALIAS))
deck_label = Label(deck_frame, image=deck_print).pack()

dealer_list_numb = IntVar()
dealer_list_numb = 1

def card_add():
    global dealer_list_numb, dealer_hand
    dealer_hand += deck[:1]
    deck.pop(0)
    dealer_list_numb += 1
    image_pick_3p = 'images/' + dealer_hand[dealer_list_numb] + '.png'
    print_image_3p = ImageTk.PhotoImage(Image.open(image_pick_3p).resize((180, 245), Image.ANTIALIAS))
    image_label[dealer_list_numb]= Label(dealer_frame, image=print_image_3p).grid(row=0, column=dealer_list_numb)
    # when pressed again the code is iterating on top of itself causing the card we just assigned/created to disapear
    # currently not adding on to hand value because we aren't calling it
    # changing it to a class system for the deck will be best if a quick fix isn't found for this

add_card = Button(root, text="add", command= card_add)
add_card.pack()




root.mainloop()