from blackjack.api.event.on_turn_event import OnTurnEvent
from blackjack.api.player import Player
from blackjack.cli.util import validate_input
from blackjack.simple.simple_player import SimplePlayer


class InteractivePlayer(SimplePlayer):
    def __init__(self, name: str):
        super().__init__(name)

    def make_turn(self, event: OnTurnEvent) -> str:
        current_value = sum(c.value for c in self.hand)
        print(f"Player[id={self._name}]: makes turn, "
              f"current sum={current_value}")
        cmd = validate_input(
            f"{self._name}, make your turn: ",
            {
                'more': 'Take one more card from Dealer.',
                'skip': 'Skip your turn.'
            }
        )
        return Player.HIT_ME if cmd == "more" else Player.SKIP
