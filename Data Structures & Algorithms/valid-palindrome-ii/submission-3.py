class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                a = s[i + 1:j+1]
                b = s[i:j]

                return self.is_palindrome(a) or self.is_palindrome(b)
            i += 1 
            j -= 1 
        
        return True 
    
    def is_palindrome(self, s:str) -> bool:
        i = 0 
        j = len(s) - 1 

        while i <= j:
            if s[i] != s[j]:
                return False 

            i += 1 
            j -= 1 
        
        return True 