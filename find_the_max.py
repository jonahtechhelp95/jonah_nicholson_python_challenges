def find_the_max(number_list):
    max_number = number_list[0]
    for number in number_list:
        if number > max_number:
            max_number = number
    return max_number

print(find_the_max([4, 9, 1, 17, 2]))
print(find_the_max([-5, -9, -2, -12]))
print(find_the_max([42]))