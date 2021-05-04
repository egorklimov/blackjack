from blackjack.api.card import Card
from blackjack.api.event.on_turn_event import OnTurnEvent
from blackjack.api.player import Player
from blackjack.simple.simple_player import SimplePlayer


def test_player_has_name():
    player: Player = SimplePlayer("test")
    assert player.name == "test"


def test_player_should_skip_turn_after_17():
    player: Player = SimplePlayer("test")
    player.add_card(Card(17, "Test", "Test card"))
    assert player.make_turn(OnTurnEvent()) == Player.SKIP


def test_player_should_skip_take_more_before_17():
    player: Player = SimplePlayer("test")
    player.add_card(Card(15, "Test", "Test card"))
    assert player.make_turn(OnTurnEvent()) == Player.HIT_ME


def test_players_hand_is_not_None():
    player: Player = SimplePlayer("test")
    assert player.show_cards() is not None


def test_players_hand_is_empty():
    player: Player = SimplePlayer("test")
    assert len(player.show_cards()) == 0


def test_it_is_not_allowed_to_add_null_card():
    player: Player = SimplePlayer("test")
    try:
        player.add_card(None)
        assert True is False
    except ValueError:
        assert True is True
