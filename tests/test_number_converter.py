from number_to_french_converter.number_converter import convert_number


def test_convert_units():
    assert convert_number(0) == "zéro"
    assert convert_number(1) == "un"
    assert convert_number(2) == "deux"
    assert convert_number(3) == "trois"
    assert convert_number(4) == "quatre"
    assert convert_number(5) == "cinq"
    assert convert_number(6) == "six"
    assert convert_number(7) == "sept"
    assert convert_number(8) == "huit"
    assert convert_number(9) == "neuf"
    assert convert_number(10) == "dix"
    assert convert_number(11) == "onze"
    assert convert_number(12) == "douze"
    assert convert_number(13) == "treize"
    assert convert_number(14) == "quatorze"
    assert convert_number(15) == "quinze"
    assert convert_number(16) == "seize"
    assert convert_number(17) == "dix-sept"
    assert convert_number(18) == "dix-huit"
    assert convert_number(19) == "dix-neuf"


def test_convert_less_than_one_hundred():
    assert convert_number(20) == "vingt"
    assert convert_number(21) == "vingt-et-un"
    assert convert_number(22) == "vingt-deux"

    assert convert_number(30) == "trente"
    assert convert_number(31) == "trente-et-un"
    assert convert_number(33) == "trente-trois"

    assert convert_number(40) == "quarante"
    assert convert_number(41) == "quarante-et-un"
    assert convert_number(44) == "quarante-quatre"

    assert convert_number(50) == "cinquante"
    assert convert_number(51) == "cinquante-et-un"
    assert convert_number(55) == "cinquante-cinq"

    assert convert_number(60) == "soixante"
    assert convert_number(61) == "soixante-et-un"
    assert convert_number(66) == "soixante-six"

    assert convert_number(70) == "soixante-dix"
    assert convert_number(71) == "soixante-et-onze"
    assert convert_number(74) == "soixante-quatorze"
    assert convert_number(77) == "soixante-dix-sept"

    assert convert_number(80) == "quatre-vingts"
    assert convert_number(81) == "quatre-vingt-un"
    assert convert_number(88) == "quatre-vingt-huit"

    assert convert_number(90) == "quatre-vingt-dix"
    assert convert_number(91) == "quatre-vingt-onze"
    assert convert_number(93) == "quatre-vingt-treize"
    assert convert_number(99) == "quatre-vingt-dix-neuf"


def test_convert_number_in_hundreds():
    assert convert_number(100) == "cent"
    assert convert_number(300) == "trois-cents"
    assert convert_number(252) == "deux-cent-cinquante-deux"
    assert convert_number(382) == "trois-cent-quatre-vingt-deux"
    assert convert_number(880) == "huit-cent-quatre-vingts"


def test_convert_number_in_thousands():
    assert convert_number(1000) == "mille"
    assert convert_number(3000) == "trois-milles"
    assert convert_number(2045) == "deux-mille-quarante-cinq"
    assert convert_number(200000) == "deux-cent-milles"
    assert convert_number(200010) == "deux-cent-mille-dix"
    assert convert_number(180000) == "cent-quatre-vingt-milles"
