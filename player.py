
class Player:
    VERSION = "V 18"
    CARD_VALUES = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11,
                   "Q": 12, "K": 13, "A": 14}

    def betRequest(self, game_state):
        players = game_state['players']
        id = game_state['in_action']
        sum = 0

        for player in players:
            if player['id'] == id:
                our_cards = player['hole_cards']
                for card in our_cards:
                    sum += player.CARD_VALUES[card["rank"]]
                if sum >= 16:
                    return game_state['current_buy_in'] - player['bet'] + game_state['minimum_raise']
                elif sum >= 12:
                    return game_state['current_buy_in'] - player['bet']

        return 0

    def showdown(self, game_state):
        pass
