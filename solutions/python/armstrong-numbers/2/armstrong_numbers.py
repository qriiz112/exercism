def is_armstrong_number(number):
    number_list = [int(x) for x in str(number)]
    number_length = len(number_list)
    return sum([x**number_length for x in number_list]) == number
