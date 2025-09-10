class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        # Always binary-search the smaller array
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        lo, hi = 0, m
        while True:
            i = (lo + hi) // 2          # elements taken from A for the left half
            j = half - i                # elements taken from B for the left half

            Aleft  = A[i-1] if i > 0 else float("-inf")
            Aright = A[i]   if i < m else float("inf")
            Bleft  = B[j-1] if j > 0 else float("-inf")
            Bright = B[j]   if j < n else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # odd
                    return float(min(Aright, Bright))
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Move partition
            if Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1

# Example usage:
sol = Solution()
print(sol.findMedianSortedArrays([1, 3,9], [2,4,6,8]))  # [1, 2, 3, 4, 6, 8, 9] -> 4
