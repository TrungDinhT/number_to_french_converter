import re
from .number_parser import (
    SmallNumberParser,
    BigNumberParser,
    FrenchDecadesAndUnitSplitter,
    SwissFrenchDecadesAndUnitSplitter,
)
from .constants import FrenchVariant, FRENCH_DECADES_DICT, SWISS_FRENCH_DECADES_DICT


class NumberConverter:
    def __init__(self, variant: FrenchVariant):
        if variant == FrenchVariant.French:
            self._decades_dict = FRENCH_DECADES_DICT
            self._decades_parser = FrenchDecadesAndUnitSplitter()
        elif variant == FrenchVariant.Swiss:
            self._decades_dict = SWISS_FRENCH_DECADES_DICT
            self._decades_parser = SwissFrenchDecadesAndUnitSplitter()

    @staticmethod
    def add_plural(number_str: str) -> str:
        if re.match("^.+-(?:vingt|cent|mille)$", number_str):
            return number_str + "s"
        return number_str

    def convert(self, val: int) -> str:
        small_number_parser = SmallNumberParser(
            decades_dict=self._decades_dict, decade_parser=self._decades_parser
        )

        if val < 1000:
            number = small_number_parser.parse(val)
        else:
            number = BigNumberParser(small_number_parser).parse(val)

        return self.add_plural(number.to_text())


def convert_number(val: int, variant: FrenchVariant = FrenchVariant.French) -> str:
    number_converter = NumberConverter(variant=variant)
    return number_converter.convert(val)
