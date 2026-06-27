class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, 0, result)
        return result  
    
    def solve(self, nums: List[int], current_index: int, result: List[int]):
        if current_index == len(nums):
            result.append(nums.copy())
            return 

        seen = set()
        for index in range(current_index, len(nums)):
            if nums[index] in seen:
                continue 
            seen.add(nums[index])
            nums[index], nums[current_index] = nums[current_index], nums[index]
            self.solve(nums, current_index + 1, result)
            nums[index], nums[current_index] = nums[current_index], nums[index]

        
             
            