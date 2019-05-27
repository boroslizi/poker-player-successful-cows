
class Player:
    VERSION = "V 18"
    CARD_VALUES = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11,
                   "Q": 12, "K": 13, "A": 14}

    def betRequest(self, game_state):
        players = game_state['players']
        id = game_state['in_action']

        for player in players:
            if player['id'] == id:
                our_cards = player['hole_cards']
                if our_cards[0]['rank'] == our_cards[1]['rank'] and Player.CARD_VALUES[our_cards[0]['rank']] >= 7:
                    return game_state['current_buy_in'] - player['bet']
                for card in our_cards:
                    if Player.CARD_VALUES[card['rank']] >= 7:
                        for com_card in game_state['community_cards']:
                            if card['rank'] == com_card['rank']:
                                return game_state['current_buy_in'] - player['bet']
                    if Player.CARD_VALUES[card['rank']] >= 10:
                        return game_state['current_buy_in'] - player['bet']

        return 0

    def showdown(self, game_state):
        pass
