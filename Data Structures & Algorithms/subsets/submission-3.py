class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, 0, [], result)
        return result 
    
    def solve(self, nums: List[int], current_index: int, current_subset: List[int], result: List[List[int]]):
        if current_index == len(nums):
            result.append(current_subset.copy())
            return 
        
        current_subset.append(nums[current_index])
        self.solve(nums, current_index + 1, current_subset, result)
        current_subset.pop()
        self.solve(nums, current_index + 1, current_subset, result)
