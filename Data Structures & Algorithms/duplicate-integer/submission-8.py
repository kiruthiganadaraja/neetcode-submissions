class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = Counter(nums)
        my_list = []
        for key,value in my_dict.items():
            if value == 2 or value > 2:
                my_list.append(value)
        print(my_list)
        print(my_dict)
        if len(my_list)> 0:
            p = True
        else:
            p = False
        return p

