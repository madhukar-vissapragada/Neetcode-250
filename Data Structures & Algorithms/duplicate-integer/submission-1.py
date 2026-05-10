class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()

        for current in nums:
            if current in result:
                return True 
                
            result.add(current)
        
        return False 
        