class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkBoxes(board)
        

    def checkRows(self, board):
        for row in range(9):
            nums = board[row]
            if not self.isNumsValid(nums):
                return False
        print('checkRows true')
        return True
    
    def checkCols(self, board):
        for col in range(9):
            nums = [board[row][col] for row in range(9)]
            if not self.isNumsValid(nums):
                return False
        print('checkCols true')
        return True

    def checkBoxes(self, board):
        for i in range(9):
            print('starting checkBoxes')
            topLeftRow = (i//3)*3
            topLeftCol = (i % 3)*3
            nums = []
            for row in range(3):
                for col in range(3):
                    nums.append(board[topLeftRow+row][topLeftCol+col])
            if not self.isNumsValid(nums):
                print('checkBoxes false')
                return False
        print('checkBoxes true')
        return True

    def isNumsValid(self, nums: List[str]):
        seen = set()
        for n in nums:
            if (n == '.'):
                continue
            if n in seen:
                return False
            seen.add(n)
        return True        