#########
# Imports
#########

from Classes import *

##################
# Global Variables
##################

game_on = True
at_war = True


###########
# Functions
###########

def play_again():
    """
    prompts for either user to select if they want to play another game.
    :return: True/False
    """
    choice = 'WRONG'

    while choice not in ['Y', 'y', 'N', 'n']:

        choice = input("play again? (Y or N): ")

        if choice not in ['Y', 'y', 'N', 'n']:
            print("invalid choice")

    if choice == 'Y' or 'y':
        return True
    else:
        return False


def rank_sum(stack):
    """
    returns the integer sum of the ranks of a stack of cards
    :param stack: list of Card() objects
    :return: integer sum.
    """

    cards_value = [0]

    for card in range(len(stack)):

        cards_value.append(stack[card].value)

    return int(sum(cards_value))


def round_stats():
    """
    prints all the stats of the cards that were played for every round
    :return: prints info.
    """

    # each player has only played one card
    if len(ceaser_played_card) < 2:

        print(f""" === Round {round_num} statistics ===
        {ceaser.name}'s card:
            card rank: {ceaser_played_card[0].rank}
            card suit: {ceaser_played_card[0].suit}
            card value: {ceaser_played_card[0].value}
            num. of cards: {len(ceaser.all_cards)}
        ----------
        {caligula.name}'s card:
            card rank: {caligula_played_card[0].rank}
            card suit: {caligula_played_card[0].suit}
            card value: {caligula_played_card[0].value}
            num. of cards: {len(caligula.all_cards)}
        """)

    # each player has played multiple cards
    elif len(ceaser_played_card) > 2:

        print(f" === Round {round_num} statistics ===")

        print(f"{ceaser.name}'s cards:")
        print(f'num. of cards: {len(ceaser.all_cards)}')
        print(f'stack total: {rank_sum(ceaser_played_card)}')
        for i in range(len(ceaser_played_card)):
            print(f"""  == Card {i} ==           
            card rank: {ceaser_played_card[i].rank}
            card suit: {ceaser_played_card[i].suit}
            card value: {ceaser_played_card[i].value}
            """)

        print(f"{caligula.name}'s cards:")
        print(f'num. of cards: {len(caligula.all_cards)}')
        print(f'stack total: {rank_sum(caligula_played_card)}')
        for i in range(len(caligula_played_card)):
            print(f"""  == Card {i} ==     
            card rank: {caligula_played_card[i].rank}
            card suit: {caligula_played_card[i].suit}
            card value: {caligula_played_card[i].value}
                 """)


######
# Main
######

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Welcome to War!')

    # generate and then shuffle a deck of cards
    caligula = Player('Lord Caligula')
    ceaser = Player('Julius Ceaser')

    new_deck = Deck()
    new_deck.shuffle()

    # deals out half the deck to each player
    for x in range(int(len(new_deck.all_cards) / 2)):
        caligula.add_cards(new_deck.deal_one())
        ceaser.add_cards(new_deck.deal_one())

    round_num = 0

    # while game_on == true, run through all this logic.
    while game_on:
        round_num += 1
        print(f'Round {round_num} ---')

        if len(caligula.all_cards) == 0:
            print(f'{caligula.name} is out of cards. {ceaser.name} is victorious!')
            print(f' this game lasted for {round_num} rounds.')
            # game_on = False
            break

        if len(ceaser.all_cards) == 0:
            print(f'{ceaser.name} is out of cards. {caligula.name} is victorious!')
            print(f' this game lasted for {round_num} rounds.')
            # game_on = False
            break

        # NEW ROUND
        ceaser_played_card = []
        caligula_played_card = []

        # draw a card from the top of each player's hand
        try:
            ceaser_played_card.append(ceaser.remove_card())
            caligula_played_card.append(caligula.remove_card())
        except IndexError as ie:
            print(ie)
            break
        print(f'{ceaser.name} played {ceaser_played_card[0]} and {caligula.name} played {caligula_played_card[0]}')

        # compare the cards
        if ceaser_played_card[0].value > caligula_played_card[0].value:
            # give ceaser the cards
            print(f"{ceaser.name}'s {ceaser_played_card[0]} wins the round.")
            ceaser.add_cards(ceaser_played_card)
            ceaser.add_cards(caligula_played_card)

            round_stats()

        elif ceaser_played_card[0].value < caligula_played_card[0].value:
            # give caligula the cards
            print(f"{caligula.name}'s {caligula_played_card[0]} wins the round.")
            caligula.add_cards(ceaser_played_card)
            caligula.add_cards(caligula_played_card)

            round_stats()

        elif ceaser_played_card[0].value == caligula_played_card[0].value:
            # if tied, then declare war; enter a at_war while loop

            while at_war:
                print(f'{ceaser.name} and {caligula.name} both played a {ceaser_played_card[0].rank}. \n'
                      f'WAR HAS BEEN DECLARED!!')

                # deals three cards to each players active pile
                for i in range(5):
                    try:
                        ceaser_played_card.append(ceaser.remove_card())
                        caligula_played_card.append(caligula.remove_card())
                    except IndexError as ie:
                        print(ie)
                        break

                # comparing the sums of each players war stack, to make it more balanced.
                if rank_sum(ceaser_played_card) > rank_sum(caligula_played_card):
                    print(f"{caligula.name}'s war stack totals {rank_sum(caligula_played_card)}, while \n"
                          f"{ceaser.name}'s war stack totals {rank_sum(ceaser_played_card)}, winning the round.")
                    ceaser.add_cards(ceaser_played_card)
                    ceaser.add_cards(caligula_played_card)
                    round_stats()
                    break

                elif rank_sum(ceaser_played_card) < rank_sum(caligula_played_card):
                    print(f"{ceaser.name}'s war stack totals {rank_sum(ceaser_played_card)}, while \n"
                          f"{caligula.name}'s war stack totals {rank_sum(caligula_played_card)}, winning the round.")
                    caligula.add_cards(caligula_played_card)
                    caligula.add_cards(ceaser_played_card)
                    round_stats()
                    break

                elif rank_sum(caligula_played_card) == rank_sum(caligula_played_card):
                    print(f"{caligula.name} and {ceaser.name} tied with a value of {caligula_played_card}. \n"
                          f"the war rages on...")
                    round_stats()

    # prompt to play again. sets game_on to false to break the big while loop
    game_on = play_again()
