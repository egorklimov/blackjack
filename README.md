# blackjack
[![CI](https://github.com/egorklimov/blackjack/actions/workflows/package.yml/badge.svg)](https://github.com/egorklimov/blackjack/actions/workflows/package.yml)

This project provides:
 * Flexible blackjack library `blackjack-lib` allowing to create a different blackjack games;
 * CLI tool to play a blackjack `blackjack-cli` locally.

## Install from source

```
python setup.py pytest && python setup.py install
blackjack-cli
```

## CLI Example
```shell
$ blackjack-cli
Welcome to CLI casino!
Please choose bot count: 2
Please, choose count of users: 1
Please choose name: Hackerman
Player[id=Dealer]: take card 7_of_Diamonds
Player[id=Dealer]: take card 9_of_Clubs
Player[id=Player_0]: take card Jack_of_Diamonds
Player[id=Player_0]: take card 4_of_Clubs
Player[id=Hackerman]: take card 6_of_Hearts
Player[id=Hackerman]: take card Jack_of_Clubs
Player[id=Player_1]: take card 5_of_Diamonds
Player[id=Player_1]: take card Ace_of_Diamonds
Player[id=Player_0]: before turn
Player[id=Player_0]: makes turn, sum=14
Player[id=Player_0]: take card 10_of_Spades
Player[id=Player_0]: made a turn
Player[id=Hackerman]: before turn
Player[id=Hackerman]: makes turn, current sum=16
Hackerman, make your turn: help
Available commands:
	more: Take one more card from Dealer.
	skip: Skip your turn.
Hackerman, make your turn: more
Player[id=Hackerman]: take card 9_of_Spades
Player[id=Hackerman]: made a turn
Player[id=Player_1]: before turn
Player[id=Player_1]: makes turn, sum=16
Player[id=Player_1]: take card 2_of_Diamonds
Player[id=Player_1]: made a turn
Player[id=Player_1]: before turn
Player[id=Player_1]: makes turn, sum=18
Player[id=Player_1]: made a turn
Player[id=Dealer]: before turn
Player[id=Dealer]: makes turn, sum=16
Player[id=Dealer]: take card 4_of_Diamonds
Player[id=Dealer]: made a turn
Player[id=Dealer]: before turn
Player[id=Dealer]: makes turn, sum=20
Player[id=Dealer]: made a turn
Leader Board:
	Dealer: 20
	Player_0: 24
	Hackerman: 25
	Player_1: 18
Results:
	Player Player_0 lost to the dealer
	Player Hackerman lost to the dealer
	Player Player_1 lost to the dealer
Thanks for playing, come again

```