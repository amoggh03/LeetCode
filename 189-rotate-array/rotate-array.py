class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Calculate effective rotation steps

        if k == 0 or n == 0 or n == 1:
            return  # No need to rotate

        def reverse_array(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Rotate the array
        reverse_array(0, n - 1)
        reverse_array(0, k - 1)
        reverse_array(k, n - 1)