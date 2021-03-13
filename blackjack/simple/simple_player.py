from typing import List

from ..api.card import Card
from ..api.event.after_turn_event import AfterTurnEvent
from ..api.event.before_turn_event import BeforeTurnEvent
from ..api.event.on_turn_event import OnTurnEvent
from ..api.player import Player


class SimplePlayer(Player):
    def __init__(self, name: str = None):
        self._name = name if name is not None else id(self)
        self.hand: List[Card] = []

    @property
    def name(self) -> str:
        return self._name

    def add_card(self, card: Card) -> None:
        print(f"Player[id={self._name}]: take card {card.name}")
        self.hand.append(card)

    def skip_turn(self) -> None:
        print(f"Player[id={self._name}]: skip turn")

    def show_cards(self) -> List[Card]:
        return self.hand

    def before_turn(self, event: BeforeTurnEvent) -> None:
        print(f"Player[id={self._name}]: before turn")

    def make_turn(self, event: OnTurnEvent) -> str:
        current_value = sum(c.value for c in self.hand)
        print(f"Player[id={self._name}]: makes turn, sum={current_value}")
        return Player.HIT_ME if current_value < 17 else Player.SKIP

    def after_turn(self, event: AfterTurnEvent) -> None:
        print(f"Player[id={self._name}]: made a turn")
