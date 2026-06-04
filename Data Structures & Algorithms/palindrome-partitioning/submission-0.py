class Solution:
    def partition(self, s: str) -> List[List[str]]:
         result = []
         self.solve(s, 0, len(s)-1, [], result)
         return result 

    
    @staticmethod
    def is_palindrome(s: str):
        start = 0 
        end = len(s) - 1 

        while start <= end:
            if s[start] != s[end]:
                return False 
            start += 1 
            end -= 1
        return True

    def solve(self, s: str, start: int, end: int, current_possibility: List[str], result: List[List[str]]):
        if start > end:
            result.append(current_possibility.copy())
            return 
        
        for index in range(start, end+1):
            if Solution.is_palindrome(s[start:index+1]):
                current_possibility.append(s[start:index+1])
                self.solve(s, index + 1, end, current_possibility, result)
                current_possibility.pop()
         
            


        