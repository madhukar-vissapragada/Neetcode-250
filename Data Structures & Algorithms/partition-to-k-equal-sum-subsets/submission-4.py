class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum %  k == 0:
            required_sum = total_sum // k
            return self.solve(nums, k, 0, [0] * len(nums), required_sum, required_sum)
        
        return False 
    

    def solve(self, nums: List[int], k: int, current_index: int, tracker: List[int], target_sum: int, req_sum: int):
        if k == 0:
            return True 
        
        if target_sum == 0:
            return self.solve(nums, k-1, 0, tracker, req_sum, req_sum)
        
        if current_index == len(nums):
            return False 
        
        for index in range(current_index, len(nums)):
            if tracker[current_index] == 0 and target_sum >= nums[index]:
                tracker[index] = 1 
                if self.solve(nums, k, index + 1, tracker, target_sum - nums[index], req_sum):
                    return True 
                tracker[index] = 0
        
        return False 

                
            