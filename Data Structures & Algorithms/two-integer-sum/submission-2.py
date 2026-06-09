class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        result = None

        for index in range(len(nums)):
            if nums[index] > target:
                target_sum = nums[index] - target
            else:
                target_sum = target - nums[index] 

            if target_sum in hash_map:
                result = [hash_map[target_sum], index]
                break 

            hash_map[nums[index]] = index

        return sorted(result)             


        