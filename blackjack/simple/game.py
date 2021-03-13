import random
from typing import MutableSet, Dict

from blackjack.api.card import Card
from blackjack.api.dealer import Dealer
from blackjack.api.event.after_turn_event import AfterTurnEvent
from blackjack.api.event.before_turn_event import BeforeTurnEvent
from blackjack.api.event.on_turn_event import OnTurnEvent
from blackjack.api.game import Game
from blackjack.api.player import Player


class SimpleGame(Game):
    def __init__(self,
                 deck: MutableSet[Card],
                 dealer: Dealer,
                 players: MutableSet[Player]):
        self._deck = deck
        self._dealer = dealer
        self._players = players
        self._turn: [int, Player] = [0, dealer]
        self._scoreboard: Dict[Player, int] = {p: 0 for p in [dealer, *players]}

    @property
    def deck(self) -> MutableSet[Card]:
        return self._deck

    @property
    def dealer(self) -> Dealer:
        return self.dealer

    @property
    def players(self) -> MutableSet[Player]:
        return self.players

    def complete(self) -> Dict[Player, int]:
        self.__start()
        if self.__get_player_score(self._dealer) == Game.BLACKJACK:
            return self._scoreboard

        for player in self._players:
            self.__handle(player)
        return self._scoreboard

    def __handle(self, player: Player) -> None:
        player.before_turn(BeforeTurnEvent())
        turn: str = player.make_turn(OnTurnEvent())

        if turn == Player.HIT_ME:
            self._dealer.send_card(player, self)
            self.__update_scoreboard(player)
            player.after_turn(AfterTurnEvent())
            if self.__get_player_score(player) < Game.BLACKJACK:
                self.__handle(player)
        elif turn == Player.SKIP:
            player.after_turn(AfterTurnEvent())
        else:
            raise AssertionError

    def __start(self) -> None:
        self._dealer.send_card(self._dealer, self)
        self._dealer.send_card(self._dealer, self)
        self.__update_scoreboard(self._dealer)

        for player in self._players:
            self._dealer.send_card(player, self)
            self._dealer.send_card(player, self)
            self.__update_scoreboard(player)

    def __update_scoreboard(self, player: Player) -> None:
        self._scoreboard[player] = self.__get_player_score(player)

    def __get_player_score(self, player: Player) -> int:
        return sum(c.value for c in player.show_cards())
