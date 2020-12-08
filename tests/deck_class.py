import random
from tkinter import *
from PIL import Image, ImageTk

root =Tk()
root.title('21 Blackjack')
root.iconbitmap('images/21_cards.ico')
root.geometry('1280x750')
root.configure(bg='green')

cards = []

suits = ['hearts', 'clubs', 'diamonds', 'spades']
face_cards = ['ace', 'jack', 'queen', 'king']

extension = 'png'

for y in suits:
    for x in range(2, 11):
        name = 'images/{}-{}.{}'.format(str(x), y, extension)
        cards.append(name)

    for x in face_cards:
        name = 'images/{}-{}.{}'.format(str(x), y, extension)
        cards.append(name)

print(cards)
print(len(cards))
random.shuffle(cards)
print(cards[0])

hand = []

def deal():
    global hand
    card_image = ImageTk.PhotoImage(Image.open(cards[0]).resize((180, 245), Image.ANTIALIAS)) # image antialias isn't required but looks better with it
    card_label = Label(root, image=card_image, relief="raised")
    card_label.image = card_image # very important! stops cards being thrown away/overwritten. Has to be before .pack()
    card_label.pack(side="left")
    hand += cards[:1]
    cards.pop(0)
    print(hand)


deal_button = Button(root, text="deal", command=deal).pack()

root.mainloop()


#### used grid to make frames (only need one for this test) and unpack side left