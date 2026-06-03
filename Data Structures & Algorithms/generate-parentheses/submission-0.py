class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] 
        self.solve(n, 0, 0, "", result)
        return result 
    

    def solve(self, n: int, open_count: int, closed_count: int, current_combination: str, result: List[str]): 
        if open_count == n and closed_count == n: 
            result.append(current_combination)
            return 
        
        if open_count < n:
            self.solve(n, open_count + 1, closed_count, current_combination + '(', result)
        if open_count > closed_count:
            self.solve(n, open_count, closed_count + 1, current_combination + ')', result)
        

