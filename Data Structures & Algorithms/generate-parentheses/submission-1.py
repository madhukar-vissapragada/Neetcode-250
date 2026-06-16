class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.solve(n, n, "", result)
        return result  
    
    def solve(self, open_count: int, close_count: int, current_combination: str, result: List[str]):
        if open_count == 0 and close_count == 0:
            result.append(current_combination)
            return
        
        if open_count:
            self.solve(open_count - 1, close_count, current_combination + "(", result)
        
        if open_count < close_count:
            self.solve(open_count, close_count - 1, current_combination + ")", result)
        
    
        