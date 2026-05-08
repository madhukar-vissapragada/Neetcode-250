class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(nums, target, 0, [], result)
        return result 
    
    def solve(self, nums, target, current_index, current_subset, result):
        if target == 0:
            result.append(current_subset.copy())
            return 

        if current_index == len(nums):
            return 

        if target >= nums[current_index]:
            current_subset.append(nums[current_index])
            self.solve(nums, target-nums[current_index], current_index, current_subset, result)
            current_subset.remove(nums[current_index])
        
        self.solve(nums, target, current_index + 1, current_subset, result)

                