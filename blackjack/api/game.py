from __future__ import annotations

import abc
from typing import MutableSet, Dict

from blackjack.api import dealer
from blackjack.api.card import Card
from blackjack.api.player import Player


class Game(metaclass=abc.ABCMeta):
    BLACKJACK = 21

    @property
    @abc.abstractmethod
    def deck(self) -> MutableSet[Card]:
        pass

    @property
    @abc.abstractmethod
    def dealer(self) -> dealer.Dealer:
        pass

    @property
    @abc.abstractmethod
    def players(self) -> MutableSet[Player]:
        pass

    @abc.abstractmethod
    def complete(self) -> Dict[Player, int]:
        pass
