from enum import StrEnum


UNITS = {
    0: "zéro",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze",
    16: "seize",
}

MILLIONS = {
    1: "mille"
    # We can add more like million, billion, etc.
}

FRENCH_DECADES_DICT = {
    10: "dix",
    20: "vingt",
    30: "trente",
    40: "quarante",
    50: "cinquante",
    60: "soixante",
    80: "quatre-vingt",
}

SWISS_FRENCH_DECADES_DICT = {
    10: "dix",
    20: "vingt",
    30: "trente",
    40: "quarante",
    50: "cinquante",
    60: "soixante",
    70: "septante",
    80: "huitante",
    90: "nonante"
}

class FrenchVariant(StrEnum):
    French = "fr"
    Swiss = "ch"
