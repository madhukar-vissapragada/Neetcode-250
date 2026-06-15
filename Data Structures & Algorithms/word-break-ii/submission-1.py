class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        configuration = []
        self.solve(s, wordDict, 0, len(s)-1, configuration, result)
        return result 
    
    def solve(self, s: str, word_dict: set, start: int, end: int, configuration: List[str], result: List[str]):
        if start == len(s):
            result.append(' '.join(configuration).strip())
            return 
        
        for index in range(start, end + 1):
            if s[start: index + 1] in word_dict:
                configuration.append(s[start: index + 1])
                self.solve(s, word_dict, index + 1, end, configuration, result)
                configuration.pop()


        