class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        configuration = []
        for row in range(n):
            configuration.append(['.'] * n)
        self.solve(n, 0, configuration, result)
        return len(result) 
    
    def solve(self, n: int, current_row: int, current_configuration: List[str], result: List[List[str]]):
        if current_row == n:
            result.append(''.join(row) for row in current_configuration)
            return 

        for current_col in range(n):
            if self.is_valid(n, current_row, current_col, current_configuration):
                current_configuration[current_row][current_col] = "Q"
                self.solve(n, current_row + 1, current_configuration, result)
                current_configuration[current_row][current_col] = "."

    def is_valid(self, n: int, current_row: int, current_col: int, configuration: List[str]):
        def is_col_valid(n: int, current_col: int, configuration: List[List[str]]):
            for row in range(n):
                if configuration[row][current_col] == "Q":
                    return False 
            return True 
        
        def is_diagonally_valid(n: int, current_row: int, current_col: int, configuration: List[List[str]]):
            # left upward 
            row = current_row 
            col = current_col

            while row >= 0 and col >= 0:
                if configuration[row][col] == "Q":
                    return False 
                
                row -= 1
                col -= 1 
            
            # right upward
            row = current_row 
            col = current_col 

            while row >= 0 and col < n:
                if configuration[row][col] == "Q":
                    return False 
                
                row -= 1 
                col += 1 

            return True 
        
        return is_col_valid(n, current_col, configuration) and is_diagonally_valid(n, current_row, current_col, configuration)
