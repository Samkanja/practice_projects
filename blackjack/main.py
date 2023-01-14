import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS =  chr(9827)

BACKSIDE = 'backside'

def main():
    money = 5000
    while True:
        if money <= 0:
            print('You\'re broke')
            sys.exit()
        print(f'Money: {money}')

        bet = get_bet(money)

        deck = get_deck()

        dealer_hand = [deck.pop(),deck.pop()]
        player_hand = [deck.pop(),deck.pop()]

        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand,money-bet)

            if move == "D":
                additinal_bet = get_bet(min(bet, (money-bet)))

                bet += additinal_bet
                print(f'Bet increased to {bet}')
                print('Bet:', bet)
            if move in ('H','D'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ('S','D'):
                break
        
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) <= 17:
                print('Dealer hits ...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand,dealer_hand,False)

                if get_hand_value(dealer_hand) > 21:
                    break
                input("Press Enter to continue...")
                print('\n\n')
            
        display_hands(player_hand,dealer_hand,True)


        player_value = get_hand_value(player_hand)

        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print(f'Dealer busts! You win ${bet}')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('you lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won ${bet}')
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie, the bet is returned to you')

        input('Press Enter to continue...')
        print('\n\n')

def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank),suit))
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def display_hands(player_hand,dealer_hand,show_dealer_hand):
    """Show the playe's and dealer's cards. Hide the dealer's first
    card if showdealerhand is False."""

    if show_dealer_hand:
        print('Dealer:', get_hand_value(dealer_hand)) 
        display_card(dealer_hand)
    else:
        print('DEALER: ???')
        display_card(player_hand)
    print('PLAYER:', get_hand_value(player_hand))
    display_card(player_hand)


def get_hand_value(cards):
    """Returns the value of cards. Face cards are worth 10, aces are worth
    11 or 1 (this function picks the most suitable ace value)."""

    value = 0

    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            number_of_aces += 1
        elif rank in ('K','Q','J'):
            value += 10
        else:
            value += int(rank)    

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10
    return value


def display_card(cards):
    """Display all the cards in the cards list."""

    rows = ['','','','']
    for i , card in enumerate(cards):
        rows[0] += '___ '
        if card == BACKSIDE:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'

        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} |'
            rows[2] += f'| {suit} |'
            rows[3] += f'|_{rank.rjust(2, "_")}'

    for row in rows:
        print(row)


def get_move(player_hand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand, and 'D' for double down."""

    while True:
        moves = ['(H)it','(S)tand']

        #The player can handle on ther first move, which can tell
        # because they'll have exactly two cards:

        if len(player_hand) == 2:
            moves.append("(D)ouble down ")
        #Get the player's move
        move_prompt = ','.join(moves) + '>'
        move = input(move_prompt).upper()
        if move in ('H','S'):
            return move
        if move == 'D':
            return move



def get_bet(max_bet):
    """Ask the player how much they want to bet for this round"""

    while True:
        print(f'How much do you bet? (1-{max_bet}, or QUIT)')
        bet = input('>').upper().strip()
        if bet == 'QUIT':
            print('Thank for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet



if __name__ == '__main__':
    main()


        