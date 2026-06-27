class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, 0, [], result)
        return result  
    
    def solve(self, nums: List[int], current_index: int, current_config: List[int], result: List[List[int]]):
        result.append(current_config.copy()) 
        
        for index in range(current_index, len(nums)):
            current_config.append(nums[index])
            self.solve(nums, index + 1, current_config, result)
            current_config.pop()
        
        
    
        