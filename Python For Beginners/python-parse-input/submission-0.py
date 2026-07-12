from typing import List

def read_integers() -> List[int]:
    input_line = (input())
    output_list = []
    output_list = input_line.split(",")
    for each in range(len(output_list)):
        output_list[each] = int(output_list[each])
    
    return output_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())