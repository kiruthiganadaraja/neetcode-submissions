class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums:
            while val in nums:
              nums.remove(val)
        final_length = len(nums)
        return final_length
