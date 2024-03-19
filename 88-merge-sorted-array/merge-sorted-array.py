class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        def join(nums1, nums2):
            nums1[m:] = nums2  # Merge nums2 into nums1
            nums1.sort()       # Sort the merged list
        
        join(nums1, nums2)