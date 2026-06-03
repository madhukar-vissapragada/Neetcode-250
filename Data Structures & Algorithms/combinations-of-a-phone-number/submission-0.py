class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        self.solve(digits, 0, "", letter_map, result)
        return result 
    

    def solve(self, digits: str, current_index: int, current_combination: str, letter_map: dict, result: List[str]):
        if current_index == len(digits):
            if current_combination != "":
                result.append(current_combination)
            return
        
        for letter in letter_map[digits[current_index]]:
            self.solve(digits, current_index + 1, current_combination + letter, letter_map, result) 
        