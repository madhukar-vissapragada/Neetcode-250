class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols
            exact_mid = matrix[row][col]

            if exact_mid == target:
                return True

            if exact_mid > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
