
class Player:
    VERSION = "V 18"

    def betRequest(self, game_state):
        players = game_state['players']
        id = game_state['in_action']

        for player in players:
            if player['id'] == id:
                our_cards = player['hole_cards']
                for card in our_cards:
                    if card['rank'] in "JQKA":
                        return game_state['current_buy_in'] - player['bet'] + game_state['minimum_raise']

        return 0

    def showdown(self, game_state):
        pass
