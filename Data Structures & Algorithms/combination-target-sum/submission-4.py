class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(nums, 0, target, [], result)
        return result  
    
    def solve(self, nums: List[int], current_index: int, target: int, 
                    current_config:List[int], 
                    result: List[List[int]]): 
        if target == 0:
            result.append(current_config.copy())
            return 
        
        if current_index == len(nums):
            return 
        
        # choose 
        if target >= nums[current_index]:
            current_config.append(nums[current_index])
            self.solve(nums, current_index, target - nums[current_index], current_config, result)
            current_config.pop()
        # not choose
        self.solve(nums, current_index + 1, target, current_config, result)

        