class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for current in strs:
                key = tuple(sorted(current))
                if key in hash_map:
                        hash_map[key].append(current)
                else:
                        hash_map[key] = [current]
        
        groups = list(hash_map.values())

        return groups         

        