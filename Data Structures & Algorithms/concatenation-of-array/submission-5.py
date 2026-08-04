class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cloned_list = nums.copy()
        final_list = nums + cloned_list
       
        return final_list
        