import random
from typing import List

import blackjack.api.dealer as dealer

from blackjack.api.card import Card
from blackjack.api.event.after_turn_event import AfterTurnEvent
from blackjack.api.event.before_turn_event import BeforeTurnEvent
from blackjack.api.event.on_turn_event import OnTurnEvent
from blackjack.api.game import Game
from blackjack.api.player import Player
from blackjack.simple.simple_player import SimplePlayer


class SimpleDealer(dealer.Dealer):
    def __init__(self, name: str = None):
        self.proxy_player: Player = SimplePlayer(name)

    @property
    def name(self) -> str:
        return self.proxy_player.name

    def send_card(self, player: Player, game: Game) -> None:
        if len(game.deck) == 0:
            raise ValueError("The deck is over")
        card: Card = random.choice(list(game.deck))
        player.add_card(card)
        game.deck.remove(card)

    def add_card(self, card: Card) -> None:
        self.proxy_player.add_card(card)

    def skip_turn(self) -> None:
        self.proxy_player.skip_turn()

    def show_cards(self) -> List[Card]:
        return self.proxy_player.show_cards()

    def before_turn(self, event: BeforeTurnEvent) -> None:
        self.proxy_player.before_turn(event)

    def make_turn(self, event: OnTurnEvent) -> str:
        return self.proxy_player.make_turn(event)

    def after_turn(self, event: AfterTurnEvent) -> None:
        self.proxy_player.after_turn(event)
