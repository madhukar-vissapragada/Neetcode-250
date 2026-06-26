class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for current in nums:
            if current in hash_set:
                return True 
            hash_set.add(current)
        
        return False 
        