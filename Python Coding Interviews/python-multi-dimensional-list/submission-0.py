from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    end_list = []
    for sublist in nested_arr:
        sublist.sort()
        end_list.append(sublist[len(sublist)-1])
    return end_list



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
