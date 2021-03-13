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
            deck = Card.create_default_mutable_deck()

        self.deck = deck
        self.dealer = dealer
        self.players = players

    def build(self) -> Game:
        return SimpleGame(self.deck, self.dealer, self.players)

    def with_dealer(self, dealer: Dealer) -> GameBuilder:
        if dealer is None:
            raise ValueError("Dealer must be not None")
        return SimpleGameBuilder(dealer, self.deck, self.players)

    def with_players(self, players: MutableSet[Player]) -> GameBuilder:
        if players is None:
            raise ValueError("Players must be not None")
        return SimpleGameBuilder(self.dealer, self.deck, players)

    def with_deck(self, deck: MutableSet[Card]) -> GameBuilder:
        if deck is None:
            raise ValueError("Deck must be not None")
        return SimpleGameBuilder(self.dealer, deck, self.players)
