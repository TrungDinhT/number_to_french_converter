import re
from .number_representation import LessThanAThousand, MoreThanAThousand


def add_plural(number_str: str) -> str:
    if re.match("^.+-(?:vingt|cent|mille)$", number_str):
        return number_str + "s"
    return number_str


def convert_number(val: int) -> str:
    if val < 1000:
        number = LessThanAThousand(val)
    else:
        number = MoreThanAThousand(val)
    return add_plural(number.to_text())
