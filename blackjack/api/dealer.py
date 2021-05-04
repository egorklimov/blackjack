import abc

from blackjack.api.game import Game
from blackjack.api.player import Player


class Dealer(Player, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send_card(self, player: Player, game: Game) -> None:
        pass
