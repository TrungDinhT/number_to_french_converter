from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from .number_representation import (
    NumberRepresentation,
    LessThanAThousand,
    MoreThanAThousand,
)
from .constants import UNITS


class NumberParser(ABC):
    @abstractmethod
    def parse(self, val: int) -> NumberRepresentation:
        pass


class DecadeParser(ABC):
    @staticmethod
    @abstractmethod
    def split_decades_and_unit(val: int) -> Tuple[List[int], int]: ...


class FrenchDecadesAndUnitSplitter(DecadeParser):
    @staticmethod
    def split_decades_and_unit(val: int) -> Tuple[List[int], int]:
        decades = []
        decade, unit = (val // 10) * 10, val % 10
        if decade in [70, 90]:
            decades.append(decade - 10)
            if unit + 10 not in UNITS:
                decades.append(10)
            else:
                unit += 10
        elif decade > 0:
            decades.append(decade)
        return decades, unit


class SwissFrenchDecadesAndUnitSplitter(DecadeParser):
    @staticmethod
    def split_decades_and_unit(val: int) -> Tuple[List[int], int]:
        decade, unit = (val // 10) * 10, val % 10
        if decade > 0:
            return [decade], unit
        else:
            return [], val


class SmallNumberParser(NumberParser):
    """Parser for numbers from 0 - 999"""

    def __init__(self, decades_dict: Dict[int, str], decade_parser: DecadeParser):
        self._decades_dict = decades_dict
        self._decade_parser = decade_parser

    def parse(self, val: int) -> LessThanAThousand:
        if val < 17:
            return LessThanAThousand(
                val=val,
                unit=val,
                decades=[],
                decades_str_dict=self._decades_dict,
            )
        else:
            decades, unit = self._decade_parser.split_decades_and_unit(val % 100)
            hundred = None if val < 100 else val // 100
            return LessThanAThousand(
                val=val,
                unit=unit,
                decades=decades,
                hundred=hundred,
                decades_str_dict=self._decades_dict,
            )


class BigNumberParser(NumberParser):
    """Parser for numbers from 1000"""

    def __init__(self, small_number_parser: NumberParser):
        self._small_number_parser = small_number_parser

    def parse(self, val: int) -> MoreThanAThousand:
        list_hundreds: List[LessThanAThousand] = []
        tmp = val
        while tmp > 0:
            list_hundreds.append(self._small_number_parser.parse(tmp % 1000))
            tmp //= 1000
        return MoreThanAThousand(val=val, list_hundreds=list_hundreds)
