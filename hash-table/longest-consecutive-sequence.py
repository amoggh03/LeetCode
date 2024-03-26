class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        check = set()
        tempCount, count = 1, 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] not in check:
                tempCount = tempCount+1 if nums[i]+1==nums[i+1]  else 1
                count = max(count, tempCount)
                check.add(nums[i])
        return count

        # ...Neetcode Solution...

        check = set(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i]-1 not in check:
                tempCount = 1
                while nums[i]+tempCount in check:
                    tempCount += 1
                count = max(count, tempCount)
        return count