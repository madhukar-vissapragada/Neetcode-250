class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        self.solve(nums, 0, target, [], result)
        return result  
    

    def solve(self, nums: List[int], current_index: int, target: int, current_combination: List[int], result: List[List[int]]):
        if target == 0:
            result.append(current_combination.copy())
            return
        
        for index in range(current_index, len(nums)):
            if index > current_index and nums[index] == nums[index - 1]:
                continue 

            if target >= nums[index]:
                current_combination.append(nums[index])
                self.solve(nums, index + 1, target-nums[index], current_combination, result)
                current_combination.pop()
    
        