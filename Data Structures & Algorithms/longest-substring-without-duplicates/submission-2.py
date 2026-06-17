class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        acquire = 0 
        release = 0 
        max_length = 0

        while acquire < len(s):
            if s[acquire] not in hash_map:
                hash_map[s[acquire]] = 1 
                max_length = max(len(hash_map), max_length)
                
                acquire += 1 
            else:
                del hash_map[s[release]]
                release += 1 
        
        return max_length