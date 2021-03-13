from typing import MutableSet

from blackjack.api.card import Card
from blackjack.api.dealer import Dealer
from blackjack.api.game import Game
from blackjack.api.game_builder import GameBuilder
from blackjack.api.player import Player
from blackjack.simple.dealer import SimpleDealer
from blackjack.simple.game import SimpleGame


class SimpleGameBuilder(GameBuilder):
    def __init__(self,
                 dealer: Dealer = None,
                 deck: MutableSet[Card] = None,
                 players: MutableSet[Player] = None):
        if dealer is None:
            dealer = SimpleDealer()
        if players is None:
            players = set()
        if deck is None:
            deck = set()

        self.deck = deck
        self.dealer = dealer
        self.players = players

    def build(self) -> Game:
        return SimpleGame(self.deck, self.dealer, self.players)

    def with_dealer(self, dealer: Dealer) -> GameBuilder:
        return SimpleGameBuilder(dealer, self.deck, self.players)

    def with_players(self, players: MutableSet[Player]) -> GameBuilder:
        return SimpleGameBuilder(self.dealer, self.deck, players)

    def with_deck(self, deck: MutableSet[Card]) -> GameBuilder:
        return SimpleGameBuilder(self.dealer, deck, self.players)
