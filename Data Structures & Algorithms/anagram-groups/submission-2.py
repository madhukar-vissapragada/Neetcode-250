class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for current in strs:
            key = ''.join(sorted(current))
            if key in hash_map:
                hash_map[key].append(current)
            else:
                hash_map[key] = [current]
        
        return list(hash_map.values())
