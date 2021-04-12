from app.roman_numerals import parse
from pytest import mark


@mark.parametrize('s,expected', [('IX', 9), ('X', 10), ('MCMLXXII', 1972)])
def test_roman_numeral_parser():
    # assert parse('IX') == 9
    result = parse(s)
    assert result == expected

# def test_roman_numeral_parser():
#     assert parse('X') == 10


# def test_roman_numeral_parser():
#     assert parse('XI') == 11


# def test_roman_numeral_parser():
#     assert parse('XIV') == 14


# def test_roman_numeral_parser():
#     assert parse('XIX') == 19


# def test_roman_numeral_parser():
#     assert parse('XX') == 20


# def test_roman_numeral_parser():
#     assert parse('XXXIV') == 34


# def test_roman_numeral_parser():
#     assert parse('XLI') == 41


# def test_roman_numeral_parser():
#     assert parse('L') == 50


# def test_roman_numeral_parser():
#     assert parse('XCIX') == 99


# def test_roman_numeral_parser():
#     assert parse('C') == 100


# def test_roman_numeral_parser():
#     assert parse('CCCXXXIII') == 333


# def test_roman_numeral_parser():
#     assert parse('DLV') == 555


# def test_roman_numeral_parser():
#     assert parse('CDXLIX') == 449


# def test_roman_numeral_parser():
#     assert parse('MCMLXXII') == 1972
