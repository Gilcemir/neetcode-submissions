class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(B) + len(A)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        lo, hi = 0, len(A) - 1
        while True: # uses while true instead of lo < hi due to usage of i and j inside loop
            i = lo + (hi - lo) // 2
            j = half - i - 2 # -1 de A e -1 de B

            # avoid edge cases by using infinity values when values goes out of index
            a_left = A[i] if i >= 0 else float("-infinity")
            b_left = B[j] if j >= 0 else float("-infinity")
            a_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            b_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                #even | par
                if total % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                #odd | impar
                return min(a_right, b_right)
            elif a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1
            