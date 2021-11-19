import re

from random import randint

from .exceptions import DiceParseError
from .constants import (
    DEFAULT_DICE_SIZE,
    DEFAULT_DICE_NUMBER,
    DEFAULT_MOD_OPERAND,
    DEFAULT_MOD_VALUE,
    MOD_OPERAND_MINUS,
)


class Dice:

    def __init__(self, sides: int = DEFAULT_DICE_SIZE):
        self._sides = sides

    def roll(self):
        return randint(1, self._sides)

    def __int__(self):
        return self.roll()

    def __str__(self):
        return str(int(self))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return int(self) + int(other)

        return int(self) + other

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return int(self) - int(other)

        return int(self) - other

    __rsub__ = __sub__

    __radd__ = __add__


class DiceRoller:
    REGEX = r'^([0-9]*)?([dD])([0-9]*)?(([-+])([0-9]+))?$'

    def __init__(
        self, dice_number: int = DEFAULT_DICE_NUMBER,
        dice_size: int = DEFAULT_DICE_SIZE,
        mod_operator: str = DEFAULT_MOD_OPERAND,
        mod_value: int = DEFAULT_MOD_VALUE
    ):
        self.dice_number = dice_number
        self.dice_size = dice_size
        self.mod_operator = mod_operator
        self.mod_value = mod_value

    @classmethod
    def parse(cls, pattern: str):
        matches = re.search(cls.REGEX, pattern)
        if not matches:
            raise DiceParseError(f'Invalid pattern "{pattern}"')

        dice_num, _, dice_size, _, mod_operator, mod_val = matches.groups()

        return cls(
            dice_number=int(dice_num or DEFAULT_DICE_NUMBER),
            dice_size=int(dice_size or DEFAULT_DICE_SIZE),
            mod_operator=mod_operator or DEFAULT_MOD_OPERAND,
            mod_value=int(mod_val or DEFAULT_MOD_VALUE)
        )

    def roll(self):
        roll_res = sum(Dice(self.dice_size) for _ in range(self.dice_number))
        modifier = self.mod_value
        if self.mod_operator == MOD_OPERAND_MINUS:
            modifier *= -1

        return roll_res + modifier

    def __str__(self):
        return f'{self.dice_number}d{self.dice_size}' \
               f'{self.mod_operator}{self.mod_value}'


def roll(pattern: str = '3d6'):
    return DiceRoller.parse(pattern).roll()
