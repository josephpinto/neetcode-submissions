class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])

        # find correct row
        l,r = 0, ROWS-1
        while l<=r:
            cand_row = (l+r)//2
            if matrix[cand_row][0] <= target <= matrix[cand_row][COLS-1]:
                l = cand_row
                break
            if matrix[cand_row][0] > target:
                r = cand_row-1
            else:
                l = cand_row+1

        if l >= ROWS or not (matrix[l][0] <= target <= matrix[l][COLS-1]):
            return False
        
        row = matrix[l]
        l,r = 0, COLS-1
        while l<=r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            if row[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False


        
