class Player:
    def __init__(self,cards=[]):
        self.cards = cards
        self.win = []
    def __str__(self): #Print player
        crntcard = ''
        for card in self.cards:
            crntcard += str(card) + " "
        return crntcard

    def hit(self):
        c = self.cards.pop()
        return c

    def winthis(self,opencards):
        for card in opencards:
            self.win.append(card)
        return self.win

def getscore(v):
    score = 0
    fcd = {'A':14, 'J':11, 'Q':12, 'K':13,
            '2':2, '3':3,'4':4, '5':5, '6':6,'7':7,'8':8,
            '9':9, '10':10}

    total = score + fcd[v]
    return total

def help_me():
    fhandler = open('war.txt','r')
    # ftext = fhandler.read()
    for line in fhandler:
        line = line.rstrip()
        print(line)

    while True:
        inp = input('Enter --resume to resume game\n')
        if inp != '--resume':
            print('Invalid input')
            continue
        else:
            break

from random import shuffle
def createDeck():
    Deck = []
    faceval = ['A','J','Q','K']
    for i in range(4): #for 4 suits
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceval:
            Deck.append(card)

    shuffle(Deck)
    return Deck

cardDeck = createDeck()
# print(cardDeck)
# print(len(cardDeck))
h1 = cardDeck[:26]
h2 = cardDeck[26:]

# print(h1)
# print(h2)
p1 = Player(h1)
p2 = Player(h2)
name = input('Enter your name>>')
print('Player2>> Computer')
opencards = []
while True:
    print(name + '\'s Turn>>')
    card = input('Press Y to hit the card\nType --help to get help on this game\n')
    if card == 'y' or card == 'Y':
        cc1 = p1.hit()
        opencards.append(cc1)
        # print('oc',opencards)
        # print('Pl1',p1)
    elif card == '--help':
        help_me()
        continue
    else:
        print('Wrong input\nPlease try again')
        continue

    cc2 = p2.hit()
    opencards.append(cc2)
    # print('oc',opencards)
    # print('Pl2',p2)
    if len(p1.cards) == 0 or len(p2.cards) == 0:
        break
    else:
        if getscore(cc1) == getscore(cc2):
            print('Its a tie\nOpen Cards',opencards)
            continue

        elif getscore(cc1) > getscore(cc2):
            print('Opencards', opencards)
            p1.winthis(opencards)
            print(name + ' wins this round.' + name + '\'s score', str(len(p1.win))+' ', end='')
            print('& Computer socre ', len(p2.win))
        else:
            print('Opencards', opencards)
            p2.winthis(opencards)
            print('Computer wins this round.' +name + '\'s score',str(len(p1.win))+' ', end = '')
            print('& Computer score ', len(p2.win))
    opencards = []

if len(p1.win) > len(p2.win):
    print(name+' won', len(p1.win))
else:
    print('Computer wins with', len(p2.win))
