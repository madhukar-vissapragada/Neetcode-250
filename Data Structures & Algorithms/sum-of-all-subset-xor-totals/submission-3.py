from functools import reduce 
from operator import xor 


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0 
        self.solve(nums, 0, 0)
        return self.ans 
    

    def solve(self, nums: List[int], current_index: int, xor_val: int) -> List[List[int]]:
        if current_index == len(nums):
            self.ans += xor_val
            return 
                
        self.solve(nums, current_index + 1, xor_val ^ nums[current_index])
        self.solve(nums, current_index + 1, xor_val)


        








