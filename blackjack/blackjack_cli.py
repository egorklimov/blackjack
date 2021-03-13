from typing import MutableSet, Dict

from blackjack.api.card import Card
from blackjack.api.dealer import Dealer
from blackjack.api.game import Game
from blackjack.api.player import Player
from blackjack.cli.interactive_player import InteractivePlayer
from blackjack.cli.util import ApplicationInterruptedException
from blackjack.simple.dealer import SimpleDealer
from blackjack.simple.game_builder import SimpleGameBuilder
from blackjack.simple.simple_player import SimplePlayer


def __create_bots() -> MutableSet[Player]:
    bots = int(input("Please choose bot count: "))
    return set([SimplePlayer(f"Player_{i}") for i in range(bots)])


def __create_user() -> Player:
    return InteractivePlayer(input("Please choose name: "))


def __create_users() -> MutableSet[Player]:
    cnt = int(input("Please, choose count of users: "))
    result = set()
    for i in range(cnt):
        result.add(__create_user())
    return result


def cli():
    deck: MutableSet[Card] = Card.create_default_mutable_deck()
    dealer: Dealer = SimpleDealer("Dealer")
    players: MutableSet[Player] = set(__create_bots() | __create_users())

    game: Game = SimpleGameBuilder() \
        .with_deck(deck) \
        .with_dealer(dealer) \
        .with_players(players) \
        .build()

    leaderboard: Dict[Player, int] = game.complete()

    print("Leader Board:")
    print("\n".join([f'\t{k}: {v}' for (k, v) in leaderboard.items()]))
    print("Results:")
    for player in players:
        result = "lost to the dealer"
        if leaderboard[dealer] < leaderboard[player] <= Game.BLACKJACK \
                and leaderboard[dealer] != Game.BLACKJACK:
            result = "defeated dealer"
        print(f"\tPlayer {player.name} {result}")


def main():
    try:
        print("Welcome to CLI casino!")
        cli()
        print("Thanks for playing, come again")
    except ApplicationInterruptedException:
        print("Game stopped, bye.")


if __name__ == "__main__":
    main()
