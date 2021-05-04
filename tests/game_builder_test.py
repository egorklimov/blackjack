from blackjack.api.card import Card
from blackjack.simple.game_builder import SimpleGameBuilder


def test_game_builder_produces_game_with_not_None_players_by_default():
    game = SimpleGameBuilder().build()
    assert game.players is not None


def test_game_builder_produces_game_with_empty_players_by_default():
    game = SimpleGameBuilder().build()
    assert len(game.players) == 0


def test_game_builder_produces_game_with_not_None_deck_by_default():
    game = SimpleGameBuilder().build()
    assert game.deck is not None


def test_game_builder_produces_game_with_default_deck_by_default():
    game = SimpleGameBuilder().build()
    assert game.deck == Card.create_default_mutable_deck()


def test_game_builder_produces_game_with_not_None_dealer_by_default():
    game = SimpleGameBuilder().build()
    assert game.dealer is not None


def test_game_builder_changes_players():
    game = SimpleGameBuilder().with_players(set()).build()
    assert len(game.players) == 0


def test_None_players_is_not_allowed():
    try:
        SimpleGameBuilder().with_players(None).build()
        assert True is False
    except ValueError:
        assert True is True


def test_None_deck_is_not_allowed():
    try:
        SimpleGameBuilder().with_deck(None).build()
        assert True is False
    except ValueError:
        assert True is True


def test_None_dealer_is_not_allowed():
    try:
        SimpleGameBuilder().with_dealer(None).build()
        assert True is False
    except ValueError:
        assert True is True


def test_game_builder_changes_deck():
    game = SimpleGameBuilder().with_players(set()).build()
    assert len(game.players) == 0
