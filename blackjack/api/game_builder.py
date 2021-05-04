from __future__ import annotations

import abc
from typing import MutableSet

from blackjack.api.card import Card
from blackjack.api.dealer import Dealer
from blackjack.api.game import Game
from blackjack.api.player import Player


class GameBuilder(abc.ABC):
    @abc.abstractmethod
    def build(self) -> Game:
        pass

    @abc.abstractmethod
    def with_dealer(self, dealer: Dealer) -> GameBuilder:
        pass

    @abc.abstractmethod
    def with_players(self, players: MutableSet[Player]) -> GameBuilder:
        pass

    @abc.abstractmethod
    def with_deck(self, deck: MutableSet[Card]) -> GameBuilder:
        pass
