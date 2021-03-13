from __future__ import annotations

import abc
from dataclasses import dataclass
from typing import ClassVar, Dict, AbstractSet, MutableSet


@dataclass(frozen=True)
class Card(metaclass=abc.ABCMeta):
    CARDS: ClassVar[Dict[int, str]] = {
        11: 'Jack',
        12: 'Queen',
        13: 'King',
        14: 'Ace'
    }

    SUITS: ClassVar[AbstractSet[str]] = {
        "Hearts", "Diamonds", "Clubs", "Spades"
    }

    value: int
    suit: str
    name: str

    @staticmethod
    def create_by_number(num: int, suit: str) -> Card:
        if num < 11:
            return Card(num, suit, f"{str(num)}_of_{suit}")
        elif num < 14:
            return Card(10, suit, f"{Card.CARDS[num]}_of_{suit}")
        elif num == 14:
            return Card(11, suit, f"{Card.CARDS[num]}_of_{suit}")
        else:
            raise ValueError("Only 2 - 10, Jack, Queen,"
                             " King, Ace cards are supported")

    @staticmethod
    def create_default_mutable_deck() -> MutableSet[Card]:
        return set(
            [
                Card.create_by_number(i, suit)
                for i in range(2, 15)
                for suit in Card.SUITS
            ]
        )
