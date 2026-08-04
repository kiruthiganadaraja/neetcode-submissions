class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        output_arr = []
        for i in range(0,length-1):
            new_arr = []
            new_arr = arr[i+1:]
            new_arr.sort(reverse=True)
            new_arr[0]
            output_arr.append(new_arr[0])
        output_arr.append(-1)
        return output_arr


        