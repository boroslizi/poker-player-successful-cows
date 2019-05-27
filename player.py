
class Player:
    VERSION = "V 18"
    CARD_VALUES = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11,
                   "Q": 12, "K": 13, "A": 14}

    def betRequest(self, game_state):
        players = game_state['players']
        id = game_state['in_action']

        for player in players:
            if player['id'] == id:
                hold_bet = game_state['current_buy_in'] - player['bet']
                our_cards = player['hole_cards']

                # raise once in the first round only
                if not game_state['community_cards']:
                    return hold_bet + game_state['minimum_raise']

                # check for pair in our hand (at least 9)
                if our_cards[0]['rank'] == our_cards[1]['rank'] and Player.CARD_VALUES[our_cards[0]['rank']] >= 9:
                    for i in range(len(game_state['community_cards'])):

                        # check for drill from our hand and the community cards
                        if our_cards[0]['rank'] == game_state['community_cards'][i]['rank']:

                            # check for poker from our hand and the community cards
                            for j in range(i+1, len(game_state['community_cards'])):
                                if our_cards[0]['rank'] == game_state['community_cards'][j]['rank']:
                                    return hold_bet + game_state['minimum_raise']*6

                            return hold_bet + game_state['minimum_raise']*3

                    return hold_bet

                # check for pair from our hand and the community cards
                for card in our_cards:
                    if Player.CARD_VALUES[card['rank']] >= 9:
                        for com_card in game_state['community_cards']:
                            if card['rank'] == com_card['rank']:
                                return hold_bet

                    # no pair, cards higher than 9 (only raise til call is less than 10% of our stack)
                    if Player.CARD_VALUES[card['rank']] >= 10 and hold_bet < player['stack']*0.1:
                        return hold_bet

        return 0

    def showdown(self, game_state):
        pass


