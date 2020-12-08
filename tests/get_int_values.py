card_value = {"images/2": 2, "images/3": 3, "images/4": 4, "images/5": 5, "images/6": 6, "images/7": 7, "images/8": 8,
              "images/9": 9, "images/10": 10, "images/king": 10, "images/queen": 10, "images/jack": 10, "images/ace": 11}

result_d = 0
dealer_hand = ["images/ace-hearts.png"]

for x in dealer_hand:
    result_d += card_value[x.split('-')[0]]

print(result_d)

#we will add images/6 etc to dictionary and have '-' as the split key. will work when dictionaries decide to behave again

###### dictionary behaviour changes if its a string item or a list item ############