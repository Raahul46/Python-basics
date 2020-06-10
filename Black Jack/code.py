import random

suits={"Hearts","Diamonds","Spades","Clubs"}
ranks={"Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"}
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

playing=True


class card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
            return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if (card.rank == "Ace"):
            self.aces += 1

    def adjust_for_aces(self):
        while (self.value > 21 and self.aces):
            self.value -= 10
            self.aces -= 1



class chips:

    def __init__(self, total=100):
            self.total = total
            self.bet = 0

    def win_bet(self):
            self.total += self.bet

    def lose_bet(self):
            self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet?:"))
        except:
            print("sorry try again")
        finally:
            if(chips.bet > chips.total):
                print("insufficient chips,You have",chips.total)
            else:
                break
def hit(deck,hand):
    pass


def some_who(player_hand, dealer_hand):
    print("PLAYER DETAILS \n")
    print("player hand value")
    print(player_hand.value, "\n")

    print("DEALER DETAILS \n")
    print("dealer_hand value")
    print(dealer_hand.value, "\n")


def hit_or_stand(deck, hand):
    while True:
        x = input("hit or stand? enter H or S:")

        if (x == 'H'):
            print("player hits\n")
            single_card = deck.deal()
            hand.add_card(single_card)
            hand.adjust_for_aces()
            return x
            break
        elif (x == "S"):
            print("Player stands\n")
            return x
            break


def player_busts(player,dealer,chips):
    print("PLAYER LOSES :((")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("PLAYER WINS!!!")
    chips.win_bet()
def dealer_bust(player,dealer,chips):
    print("DEALER LOSES :((")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!!!")
    chips.lose_bet()

def main():
  while True:
    print("Welcome to Black Jack")
    Deck = deck()
    player_hand = hand()
    player_hand.add_card(Deck.deal())
    player_hand.add_card(Deck.deal())

    dealer_hand = hand()
    dealer_hand.add_card(Deck.deal())
    dealer_hand.add_card(Deck.deal())

    player_chips = chips()

    take_bet(player_chips)

    some_who(player_hand, dealer_hand)

    while playing:

       var=hit_or_stand(Deck, player_hand)


       if player_hand.value > 21:
           some_who(player_hand, dealer_hand)
           player_busts(player_hand, dealer_hand, player_chips)
           print("\n"*10)
           break

       if player_hand.value == 21:
           some_who(player_hand, dealer_hand)
           player_wins(player_hand, dealer_hand,player_chips)
           print("\n" * 10)
           break
       elif(player_hand.value<21 and var=="S"):
           dealer_hand.add_card(Deck.deal())


           if dealer_hand.value > 21:
               some_who(player_hand, dealer_hand)
               dealer_bust(player_hand, dealer_hand, player_chips)
               print("\n" * 10)

               break

           if dealer_hand.value == 21:
               some_who(player_hand, dealer_hand)
               dealer_wins(player_hand, dealer_hand, player_chips)
               print("\n" * 10)

               break
           else:
               some_who(player_hand, dealer_hand)
               continue
       else:
           some_who(player_hand, dealer_hand)
           continue

if __name__ == '__main__':
    main()
