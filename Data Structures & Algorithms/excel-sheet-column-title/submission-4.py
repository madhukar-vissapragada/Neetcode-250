class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        map = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        def solve(column_number):
            if column_number >=1 and column_number < 27:
                return map[column_number] 
            
            remainder = column_number % 26 
            quotient  = column_number // 26 

            if remainder == 0:
                return f"{solve(quotient - 1)}Z"
            
            return f"{solve(quotient)}{map[remainder]}"

        return solve(columnNumber)