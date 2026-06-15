class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        configuration = [['.'] * n for _ in range(n)]
        self.solve(0, configuration, result, n)
        return len(result)
    
    def solve(self, current_row: int, current_configuration: int, result: List[List[str]],  n: int):
        if current_row == n:
            result.append(current_configuration)
            return 
        
        for current_col in range(n):
            if self.is_valid(current_row, current_col, current_configuration, n):
                current_configuration[current_row][current_col] = 'Q'
                self.solve(current_row + 1, current_configuration, result, n)
                current_configuration[current_row][current_col] = '.'
         
    

    def is_valid(self, current_row: int, current_col: int, configuration: List[List[str]], n: int):
        def is_row_valid(current_col: int, configuration: List[List[str]], n: int):
            for row in range(n):
                if configuration[row][current_col] == 'Q':
                    return False 
            
            return True 
        
        def is_diagonally_valid(current_row: int, current_col: int, configuration: List[List[str]], n: int):
            row = current_row
            col = current_col 

            while row >= 0 and col >= 0:
                if configuration[row][col] == 'Q':
                    return False 
                
                row -= 1 
                col -= 1 
            
            row = current_row 
            col = current_col 

            while row >= 0 and col < n:
                if configuration[row][col] == 'Q':
                    return False 
                
                row -= 1 
                col += 1
            
            return True 
        

        return (is_row_valid(current_col, configuration, n) and 
                is_diagonally_valid(current_row, current_col, configuration, n))
         






