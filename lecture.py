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
        print(f'stack total: {caligula_played_card}')
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
            print(f'{caligula} is out of cards. {ceaser} is victorious!')
            game_on = False
            break

        if len(ceaser.all_cards) == 0:
            print(f'{ceaser} is out of cards. {caligula} is victorious!')
            game_on = False
            break

        # NEW ROUND
        ceaser_played_card = []
        caligula_played_card = []

        at_war = True

        while at_war:

            # caligula beats ceaser
            if caligula_played_card[-1].value > ceaser_played_card[-1].value:

                caligula.add_cards(caligula_played_card)
                caligula.add_cards(ceaser_played_card)

                at_war = False

            elif caligula_played_card[-1].value < ceaser_played_card[-1].value:

                ceaser.add_cards(caligula_played_card)
                ceaser.add_cards(ceaser_played_card)

                at_war = False

            else:
                print("war!!")

                if len(ceaser.all_cards) < 3:
                    print(f"{ceaser.name} unable to declare war. {caligula.name} wins!")
                    game_on = False
                    break

                elif len(caligula.all_cards) < 3:
                    print(f"{caligula.name} unable to declare war. {ceaser.name} wins!")
                    game_on = False
                    break

                # war
                else:
                    for num in range(3):
                        caligula_played_card.append(caligula.remove_card())
                        ceaser_played_card.append(ceaser.remove_card())


