class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        
        l,r = 0, len(A)-1
        total = len(nums1) + len(nums2)
        half = total // 2
        # will always find a median

        # [AAA][AAAA]
        # [BBB][BBBB]
        while True:
            mid = (l+r)//2
            j = half - (mid + 1) - 1
            ALeft = A[mid] if mid >= 0 else float('-inf')
            ARight = A[mid+1] if mid+1 < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j+1] if j+1 < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                # odd - right partitions are bigger
                if total % 2:
                    return min(ARight,BRight)
                # even:
                return (max(ALeft,BLeft)+min(ARight,BRight)) / 2
            elif ALeft > BRight:
                r = mid - 1
            else:
                l = mid + 1


