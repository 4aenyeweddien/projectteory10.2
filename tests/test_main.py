# from src.main import divide, calculate_logarithm, reverse_string
# import pytest
#
#
# def test_divide():
#     assert divide(2, 1) == 2
#
#
# def test_zero_divide():
#     assert divide(2, 0) == 0
#
#
# def test_calc_log():
#     assert calculate_logarithm(8, 2) == 3.0
#     assert calculate_logarithm(8, 4) == 1.5
#
#     with pytest.raises(ValueError):
#         assert calculate_logarithm(0, 2)
#
#     with pytest.raises(ValueError):
#         assert calculate_logarithm(8, 0)
#
#
# @pytest.mark.parametrize('value, expected', [
#     ('123', '321'),
#     ('hello', 'olleh'),
#     ('world', 'dlrow')
# ])
# def test_reverse_string(value, expected):
#     assert reverse_string(value) == expected

# def test_reverse_string_number(numbers):
#     assert reverse_string('123') == numbers
#
#
# def test_reverse_string_letters(letters):
#     assert reverse_string('hello') == letters
#
# from src.main import finder
#
#
# def test_finder_basic():
#     assert finder([1, '2', [], {}, ('3',)], int) == 1
#     assert finder([1, '2', [], {}, ('3',), 3], int) == 2
#
#
# def test_finder_zero():
#     assert finder([1, 2, [], {}, ('3',)], str) == 0
#
#
# def test_finder_empty():
#     assert finder([], str) == 0
#
#
# def test_finder_not_list():
#     assert finder(123, int) == 0
