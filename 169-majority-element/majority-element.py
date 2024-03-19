from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        for i, j in count.items():
            if j>(len(nums)/2):
                return i
        