class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, rRow = 0, len(matrix)-1

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        while lRow <= rRow:
            mid = (lRow+rRow)//2
            candidate = matrix[mid][0]
            if candidate == target:
                return True
            if candidate > target:
                rRow = mid-1
            else:
                lRow = mid+1

        lCol, rCol = 0, len(matrix[0])-1
        while lCol <= rCol:
            midCol = (lCol+rCol)//2
            candidate = matrix[rRow][midCol]
            if candidate == target:
                return True
            if candidate > target:
                rCol = midCol-1
            else:
                lCol = midCol+1
        return False