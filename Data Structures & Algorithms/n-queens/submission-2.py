class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        current_configuration = []
        for current in range(n):
            current_configuration.append(['.'] * n)

        self.solve(0, current_configuration, result, n)
        return result 
    

    def solve(self, current_row: int, current_configuration: List[List[str]], result: List[List[str]], n: int):
        if current_row == n:
            result.append([''.join(row) for row in current_configuration])
            return 
    
        for current_col in range(n):
            if self.is_valid(current_row, current_col, current_configuration, result, n):
                current_configuration[current_row][current_col] = 'Q'
                self.solve(current_row + 1, current_configuration, result, n)
                current_configuration[current_row][current_col] = '.'

        return result

    def is_valid(self, current_row: int, current_col: int, current_configuration: List[List[str]], result: List[List[str]], n: int):
        def is_row_valid(current_col: int, current_configuration: List[List[str]], n: int):
            for row in range(n):
                if current_configuration[row][current_col] == 'Q':
                    return False 

            return True 

        
        def is_diagonally_valid(current_row: int, current_col: int, 
                                current_configuration: List[List[int]], n: int):
            # up_left 
            row = current_row
            col = current_col 

            while row >= 0 and col >= 0:
                if current_configuration[row][col] == "Q":
                    return False 
                
                row -= 1 
                col -= 1
            
            # up right
            row = current_row
            col = current_col 

            while row >= 0 and col < n:
                if current_configuration[row][col] == "Q":
                    return False 
                
                row -= 1
                col += 1

            return True 

        return (is_row_valid(current_col, current_configuration, n)
                and is_diagonally_valid(current_row, current_col, current_configuration, n))
        

            
