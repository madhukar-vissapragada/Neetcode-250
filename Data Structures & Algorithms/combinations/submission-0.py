class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [val for val in range(1, n+1)]
        self.solve(nums, k, 0, [], result)
        return result 
    
    
    def solve(self, nums: List[int], k: int, current_index: int, current_subset: List[int], result: List[List[int]]):
        if len(current_subset) > k:
            return 

        if current_index == len(nums):
            if len(current_subset) == k:
                result.append(current_subset.copy())
            return 
        

        current_subset.append(nums[current_index])
        self.solve(nums, k, current_index + 1, current_subset, result)
        current_subset.pop()
        self.solve(nums, k, current_index + 1, current_subset, result)
