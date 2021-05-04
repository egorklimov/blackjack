import abc
from typing import List

from blackjack.api.card import Card
from blackjack.api.event.after_turn_event import AfterTurnEvent
from blackjack.api.event.before_turn_event import BeforeTurnEvent
from blackjack.api.event.on_turn_event import OnTurnEvent


class Player(metaclass=abc.ABCMeta):
    HIT_ME = "hit_me"
    SKIP = "skip"

    def __repr__(self):
        return self.name

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def add_card(self, card: Card) -> None:
        pass

    @abc.abstractmethod
    def skip_turn(self) -> None:
        pass

    @abc.abstractmethod
    def show_cards(self) -> List[Card]:
        pass

    @abc.abstractmethod
    def before_turn(self, event: BeforeTurnEvent) -> None:
        pass

    @abc.abstractmethod
    def make_turn(self, event: OnTurnEvent) -> str:
        pass

    @abc.abstractmethod
    def after_turn(self, event: AfterTurnEvent) -> None:
        pass
