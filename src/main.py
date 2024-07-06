def calculate_tax(price: float, tax_rate: float) -> float:
    if price < 0:
        raise ValueError('Неверная цена')

    if 0 > tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    tax = price * tax_rate / 100
    return tax


if __name__ == '__main__':
    assert calculate_tax(500, 10) == 50

# def add_numbers(a, b):
#     return a + b
#
#
# def is_even(a):
#     return a % 2 == 0
#
#
# def find_max(my_list):
#     if len(my_list) > 0:
#         return max(my_list)
#     return 0
#
#
# if __name__ == '__main__':
#     assert add_numbers(2,2) == 4
#
#     assert is_even(0) == True
#
#     assert find_max([1, 2, 3, 4, 5]) == 5
#     assert find_max([]) == 0

# import math
#
#
# def divide(a, b):
#     if b > 0:
#         return a / b
#     return 0
#
#
# def calculate_logarithm(x, base):
#     return math.log(x, base)
#
#
# def reverse_string(my_string):
#     return my_string[::-1]


# def calc_avg(my_list):
#     if len(my_list) > 0:
#         return sum(my_list) / len(my_list)
#     return 0
#
#
# if __name__ == '__main__':
#     assert calc_avg([1, 2, 3, 4]) == 2.5
#
#     assert calc_avg([]) == 0


# def finder(my_list, my_type):
#     counter = 0
#     if isinstance(my_list, list):
#         for item in my_list:
#             if isinstance(item, my_type):
#                 counter += 1
#     return counter
