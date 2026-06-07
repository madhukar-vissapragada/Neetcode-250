from typing import *

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        req_sum = total_sum // k
        already_opted = [0] * len(nums)
        return self.solve(nums, k, 0, req_sum, req_sum, already_opted)

    def solve(self, nums, k, current_index, target_sum, req_sum, already_opted):
        if k == 0:
            return True
        if target_sum == 0:
            return self.solve(nums, k-1, 0, req_sum, req_sum, already_opted)
        if current_index == len(nums):
            return False

        for i in range(current_index, len(nums)):       # ✅ try all remaining
            if already_opted[i] == 0 and target_sum >= nums[i]:
                already_opted[i] = 1
                if self.solve(nums, k, i+1, target_sum - nums[i], req_sum, already_opted):
                    return True
                already_opted[i] = 0

        return False