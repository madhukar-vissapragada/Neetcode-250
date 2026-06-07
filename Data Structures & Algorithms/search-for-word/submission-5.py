from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if self.solve(board, word, i, j, 0, rows, cols):
                    return True
        return False

    def solve(self, board: List[List[str]], word: str,
              current_row: int,
              current_col: int,
              current_index: int,
              rows: int, cols: int):
        if current_index == len(word):
            return True

        if current_row not in range(rows) or current_col not in range(cols):
            return False
        
        if board[current_row][current_col] == '#':
            return False 

        if word[current_index] != board[current_row][current_col]:
            return False

        if word[current_index] == board[current_row][current_col]:
            board[current_row][current_col] = '#'
            up = self.solve(board, word, current_row - 1, current_col, current_index + 1, rows, cols)
            left = self.solve(board, word, current_row, current_col - 1, current_index + 1, rows, cols)
            right = self.solve(board, word, current_row, current_col + 1, current_index + 1, rows, cols)
            bottom = self.solve(board, word, current_row + 1, current_col, current_index + 1, rows, cols)

            board[current_row][current_col] = word[current_index]

            return right or bottom or left or up


        return False 
