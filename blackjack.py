#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal
import os
import configparser
import sys
from time import sleep
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

#TODO
#add min and max bets
#split deck
#ncurses display option
#add flat betting config option
#add multiple decks
#add "shuffling"
#play animation if you hit blackjack/win/loss
#Blackjack should pay out 3/2
#Mode to train for basic strategy
#Add insurance optiona
#Change tie to push
#display probabilities of each card draw
#end game when out of chips or if can't bet min amount
#fix blackjack for only natural blackjacks and not after multi hits (sum of first two cards has to be 21)
#Kill process on ctrl-c
PID = os.getpid()
def signal_handler(sig, frame):
    os.kill(PID, signal.SIGKILL)
signal.signal(signal.SIGINT, signal_handler)
os.system('cls' if os.name == 'nt' else 'clear')
__version__ = "1.0"
__author__  = "Radon Gas"
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2020 Radon Gas (radonintro1234)'

"""

Author  : Radon Gas (radonintro1234)
Github  : https://github.com/radonintro1234
License : MIT


Copyright (c) 2020 Radon Gas (radonintro1234)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
from random import shuffle

suits = ("\u2764", "\u2663", "\u25C6", "\u2660")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" :7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11}

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Card:

    """
    This Class creates a Card of a particular Suit and Rank.
    """

    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        """
        Printing a Card
        """
        return self.rank + " " + self.suit

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Deck:
    """
    This Class creates a DECK, to be used while playing a game.
    """

    def __init__(self):

        self.cardlist = []


        #CREATING A DECK {LIST} OF CARDS FOR A GAME.

        for suit in suits:
            for rank in ranks:

                current_card = Card(rank,suit)

                self.cardlist.append(current_card)


    def __str__(self):
        """
        PRINTING A DECK.
        """

        deck_cards = ''

        for x in range(len(self.cardlist)):
            deck_cards += self.cardlist[x].__str__() + "\n"

        return f"This Deck has {str(len(self.cardlist))} Cards.\n" + deck_cards

    def shuffle_deck(self):
        """
        Function For Shuffling a DECK.
        """
        shuffle(self.cardlist)

    def deal_one(self):
        """
        Function for Dealing a Card.
        """
        return self.cardlist.pop(0)

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Player():
    """
    This class is used to generate a Player.
    """

    def __init__(self,name,chips):

        self.name = name
        self.chips = chips
        self.bet = 0

    def __str__(self):
        """
        Printing a player Chips

        """
        print_statement = 'Player {} has {} chips\n'.format(self.name,self.chips)
        return print_statement

    def add_chips(self,chips):
        """
        Adding Chips to the Player
        """

        self.chips += chips

    def remove_chips(self,chips):
        """
        Removing Chips from the Player
        """

        if chips > self.chips:
            print("Unsufficient Chips.")
            print("Current balance = {}".format(self.chips))

        else:
            self.chips -= chips
            print("Current balance = {}".format(self.chips))

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class Hand():
    """
    This class is used to generate a hand for the player and the dealer
    """

    def __init__(self):

        self.cards = []
        self.value = 0
        self.ace_count = 0

    def __str__(self):
        """
        Printing a hand
        """

        cards_in_hand = 'Card list is : \n'
        for x in range(len(self.cards)):
            cards_in_hand += str(self.cards[x]) + "\n"

        return "This hand has a value of {}.\n\n".format(self.value) + cards_in_hand

    def add_card(self,card):
        """
        Adding a Card to a hand.
        """

        self.cards.append(card)
        self.value += card.value

        if card.rank == "A":
            self.ace_count += 1

        while self.value > 21 and self.ace_count > 0:
            self.value -= 10
            self.ace_count -= 1

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def take_bet(player):
    """
    Function to take a bet from the player.
    """

    while True:

        try:
            current_bet = input("How many Chips would you like to bet : ")
            if(current_bet == ''):
                if(player.bet > 0):
                    current_bet = player.bet
                else:
                    raise ValueError('oops!')
            else:
                current_bet = int(current_bet)
        except:
            print("Enter a Valid Number of Chips.")

        else:
            if current_bet > player.chips:
                print("Unsufficient Amount. Please try again.")
            else:
                player.bet = current_bet
                player.chips -= current_bet
                os.system('cls' if os.name == 'nt' else 'clear')
                break

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def double_bet(player):
    """
    Function to take a bet from the player.
    """

    if player.bet > player.chips:
        print("Unsufficient Amount. Please try again.")
    else:
        player.chips -= player.bet
        player.bet += player.bet
    global doubled
    doubled = True


'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


def create_player():
    """
    Funtion to create a Player.
    """

    global player

    config = configparser.ConfigParser()
    config.read('conf.ini')
    if(config['DEFAULT']['playername']):
        player_name = config['DEFAULT']['playername']
    else:
        while True:
            player_name = input("\n\nEnter Your Name : ")

            if player_name != '':
                break
        else:
            print("Enter a valid name.\n")

    if(config['DEFAULT']['amountofchips']):
        start_amount = int(config['DEFAULT']['amountofchips'])
    else:
        while True:
            try:
                start_amount = int(input("Enter starting number of Chips : "))
            except:
                print("Please Enter a valid Number.\n")
            else:
                break

    player = Player(player_name,start_amount)

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def adjust_winnings(winner):
    """
    Function to adjust chips at the End of the game.
    """
    global doubled
    if winner == "player":
        player.chips += int(player.bet*2)
        if(doubled == True):
            player.bet = int(player.bet/2)

    elif winner == "tie" :
        player.chips += player.bet

    elif winner == "p_blackjack" :
        player.chips += int(player.bet*3/2)



'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def hit_or_stand(player_hand,deck_1,player):
    """
    Function to give Player a choice to HIT or STAND.
    """

    global player_playing

    global doubled
    doubled = False

    while True:

        #temp = input("HIT STAND OR DOUBLE? : ")
        print("HIT STAND OR DOUBLE? : " )
        temp = getch()
        if temp == '':
            print("Please Choose a valid option.\n")
            #sleep to catch kill signal before returing to getch
            sleep(1)

        if temp[0].lower() == 'h':
            player_hand.add_card(deck_1.deal_one())
            break

        elif temp[0].lower() == 's':
            player_playing = False
            break

        elif temp[0].lower() == 'd':
            double_bet(player)
            player_hand.add_card(deck_1.deal_one())
            player_playing = False
            break

        else :
            print("Please Choose a valid option.\n")
            sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    if temp[0].lower() == 'h':
        return "h"
    else :
        return "s"

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def player_busted():
    """
    Final Winner : Dealer
    """

    global winner

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nPlayer Busted.")
    print("Dealer Wins!\n")
    winner = "dealer"

def dealer_busted():
    """
    Final Winner : Player
    """

    global winner

    print("\nDealer Busted.")
    print("Player Wins!\n")
    winner = "player"

def player_dealer_tie():
    """
    Final Winner : Tie
    """

    global winner

    print("IT'S A TIE!!\n")
    winner = "tie"

def player_wins():
    """
    Final Winner : Player
    """

    global winner

    print("Player Wins!\n")
    winner = "player"

def player_blackjack():
    """
    Final Winner : Player
    """

    global winner

    print("Blackjack!\n")
    winner = "p_blackjack"


def dealer_wins():
    """
    Final Winner : Dealer
    """

    global winner

    print("Dealer Wins!")
    winner = "dealer"

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def show_some_cards(player_hand, dealer_hand):
    """
    Function to show both hands while Hiding one of dealers Cards.
    """
    print("Current bet: " + str(player.bet))
    print("\nPlayer Cards are: ")
    for card in player_hand.cards:
        print("  " + str(card))

    print("Total value: " + str(player_hand.value))
    print("\n\nDealer Cards are: ")
    print("  " + str(dealer_hand.cards[0]))
    print("**Card is Hidden.**")
    print("Shown value: " + str(dealer_hand.cards[0].value))
    print("\n--------------------------------------------------------------------------------------------------------------------\n")

def show_all_cards(player_hand, dealer_hand):
    """
    Function to show both hands
    """

    print("\nPlayer Cards are: ")
    for card in player_hand.cards:
        print("  " + str(card))
    print("Total value: " + str(player_hand.value))

    print("\nDealer Cards are: ")
    for card in dealer_hand.cards:
        print("  " + str(card))
    print("Total value: " + str(dealer_hand.value))
    print("\n--------------------------------------------------------------------------------------------------------------------\n")

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def main(player):
    """
    Starting the main game.
    """

    #INITIALIZE A DECK OF CARDS AND SHUFFLE THEM.
    deck_1=Deck()
    deck_1.shuffle_deck()

    #CREATE PLAYER AND DEALER HANDS.
    player_hand = Hand()
    dealer_hand = Hand()

    print(player)

    #TAKE A BET FROM THE PLAYER.
    take_bet(player)

    #DEAL TWO CARDS TO PLAYER AND DEALER EACH.
    player_hand.add_card(deck_1.deal_one())
    player_hand.add_card(deck_1.deal_one())

    dealer_hand.add_card(deck_1.deal_one())
    dealer_hand.add_card(deck_1.deal_one())

    #SHOW PLAYERS CARDS AND HIDE DEALERS ONE CARD.
    show_some_cards(player_hand, dealer_hand)

    #ASK THE PLAYER TO HIT OR STAND.

    player_playing = True
    dealer_playing = True

    while player_playing == True:

        if( (player_hand.cards[0].value + player_hand.cards[1].value) == 21):
            if((dealer_hand.cards[0].value + dealer_hand.cards[1].value) == 21):
                player_dealer_tie()
            else:
                player_blackjack()
            dealer_playing = False
            break

        if player_hand.value > 21:
            player_busted()
            break

        req = hit_or_stand(player_hand, deck_1, player)

        if req == 's' or req == 'd':
            break

        show_some_cards(player_hand, dealer_hand)

    show_all_cards(player_hand, dealer_hand)

    #DEALERS TURN


    while dealer_playing:

        if player_hand.value <= 21:

            while dealer_hand.value <17 :
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nDealer Hits......")
                dealer_hand.add_card(deck_1.deal_one())
                show_all_cards(player_hand, dealer_hand)

            dealer_playing = False

            if dealer_hand.value > 21:
                dealer_busted()
                break

            elif player_hand.value == dealer_hand.value:
                player_dealer_tie()
                break

            elif player_hand.value > dealer_hand.value:
                player_wins()
                break

            else:
                dealer_wins()
                break

        else:
            break

    adjust_winnings(winner)

    print("\n" + str(player))


'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def play_again():
    """
    Asking the Player to play again.
    """

    while True:

        print("\n--------------------------------------------------------------------------------------------------------------------\n")
        temp = input("\nWant to play again? : ")

        if temp[0].lower() == 'y':
            return True
            break

        elif temp[0].lower() == 'n':
            print("\n--------------------------------------------------------------------------------------------------------------------\n")
            print("\nThank You for playing...\n")
            print("\n--------------------------------------------------------------------------------------------------------------------\n")
            return False
            break

        else :
            print("Please Choose a valid option.\n")

'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


if __name__ == '__main__':

    playing = True
    create_player()

    while playing:
        main(player)


