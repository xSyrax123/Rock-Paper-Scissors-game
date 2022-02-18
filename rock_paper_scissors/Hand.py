from enum import Enum


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
       return self.name.title()