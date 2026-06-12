class Solution:
    map = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber in range(1, 27):
            return self.map[columnNumber]

        remainder = columnNumber % 26
        quotient = columnNumber // 26

        if remainder == 0:
            return f"{self.convertToTitle(quotient - 1)}Z"

        return f"{self.convertToTitle(quotient)}{self.map[remainder]}"