class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for current in nums:
            if count == 0:
                element = current 

            if element == current:
                count += 1 
            else:
                count -= 1 

        return element  
        