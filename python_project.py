def average(my_list: list):

    count = 0
    summary = 0

    for number in  my_list:
        count += 1
        summary += number

    result = summary / count
    if result == round(result):
        return round(result)
    return result

def median(my_list: list):
    my_list.sort()
    if len(my_list) %2 == 1:
        result = my_list[len(my_list) // 2]
    else:
        result = (my_list[len(my_list) // 2 - 1] + my_list[len(my_list) // 2]) / 2

    if result == round(result):
        return round(result)
    return result

def find_max_number(my_list: list):
    max_number = my_list[0]

    for number in my_list:
        if number > max_number:
            max_number = number

    if max_number == round(max_number):
        return round(max_number)
    return max_number

def find_min_number(my_list: list):
    min_number = my_list[0]

    for number in my_list:
        if number < min_number:
            min_number = number

    if min_number == round(min_number):
        return round(min_number)
    return min_number

