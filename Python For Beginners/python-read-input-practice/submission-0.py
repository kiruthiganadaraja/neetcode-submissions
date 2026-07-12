def add_two_numbers() -> int:
    input_str = input()
    op_list = []
    # Split the input string by comma and convert each part to an integer
    for each_str in input_str.split(','):
       each = int(each_str.strip()) # .strip() to remove any whitespace
       op_list.append(each)
    result = sum(op_list)
    return result





# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())