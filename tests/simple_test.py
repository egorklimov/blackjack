from blackjack.simple.simple_player import SimplePlayer


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def test():
    SimplePlayer("a")
