class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if self.solve(board, word, row, col, rows, cols, 0):
                    return True 
        
        return False 


    def solve(self, board: List[List[str]], word: str, current_row: int, current_col: int, 
                    rows: int, cols: int, current_index: int) -> bool: 
        if current_index == len(word):
            return True
        
        if (current_row < 0 or current_row >= rows) or (current_col < 0 or current_col >= cols):
            return False 
        
        up = left = down = right = False 
        if board[current_row][current_col] == word[current_index]:
            board[current_row][current_col] = -1

            # up 
            up = self.solve(board, word, current_row - 1, current_col, rows, cols, current_index + 1)
            # down
            down = self.solve(board, word, current_row + 1, current_col, rows, cols, current_index + 1)
            # left 
            left = self.solve(board, word, current_row, current_col - 1, rows, cols, current_index + 1)
            # right 
            right = self.solve(board, word, current_row, current_col + 1, rows, cols, current_index + 1)

            board[current_row][current_col] = word[current_index]

        return up or down or left or right
    


