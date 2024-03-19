class Solution(object):
    def removeDuplicates(self, nums):
	
        if len(nums) < 2:
            return len(nums)
        
        current = 0
        for next in range(1, len(nums)):
            if nums[next] != nums[current] :
                current += 1
                nums[current] = nums[next];            
        
        return current + 1