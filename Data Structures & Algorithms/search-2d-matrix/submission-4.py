class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        row = None
        while l<=r:
            mid = (l+r)//2
            num = matrix[mid][0]
            if num <= target <= matrix[mid][-1]:
                row = mid
                break
            if num > target:
                r = mid-1
            else:
                l = mid+1
        if row is None:
            return False
        
        row_list = matrix[row]
        l,r = 0, len(row_list)-1
        while l<=r:
            mid = (l+r)//2
            num = row_list[mid]
            if num == target:
                return True
            if num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False