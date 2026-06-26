class Solution:
    def totalNQueens(self, n: int) -> int:
        self.output = 0
        grid = [['.'] * n for _ in range(n)]
        self.solve(n, grid, 0) 

        return self.output

    def solve(self, n: int, grid: List[List[str]], current_row: int):
        if current_row == n:
            self.output += 1 
            return 
        
        for current_col in range(n):
            if Solution.is_valid(grid, current_row, current_col, n):
                grid[current_row][current_col] = 'Q'
                self.solve(n, grid, current_row + 1) 
                grid[current_row][current_col] = '.'

    @staticmethod
    def is_valid(grid: List[List[str]], current_row: int, current_col: int, n: int):
        def is_row_valid(grid: List[List[str]], current_row: int, n: int):
            for current_col in range(n):
                if grid[current_row][current_col] == 'Q':
                    return False     
            return True 
        
        def is_col_valid(grid: List[List[str]], current_col: int, n: int): 
            for current_row in range(n):
                if grid[current_row][current_col] == 'Q':
                    return False 
            return True 
        
        def is_diagonally_valid(grid: List[List[str]], current_row: int, current_col: int, n: int):
            # left top 
            row = current_row 
            col = current_col 

            while row >= 0 and col >= 0:
                if grid[row][col] == 'Q':
                    return False
                
                row -= 1 
                col -= 1 
            
            # right top 
            row = current_row 
            col = current_col 
            
            while row >= 0 and col < n:
                if grid[row][col] == 'Q':
                    return False 
                
                row -= 1 
                col += 1 
            
            return True 
        
        return (is_row_valid(grid, current_row, n) and 
                is_col_valid(grid, current_col, n) and 
                is_diagonally_valid(grid, current_row, current_col, n))
