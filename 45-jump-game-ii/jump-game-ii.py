class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize pointers l and r to represent the current range of indices
        l, r = 0, 0
        # Initialize the variable to count the number of jumps
        ans = 0
        # Continue until the right pointer reaches or exceeds the last index
        while r < (len(nums) - 1):
            # Initialize the maximum jump distance
            maxJump = 0
            # Iterate through indices from l to r
            for i in range(l, r + 1):
                # Update the maximum jump distance within the current range
                maxJump = max(maxJump, i + nums[i])
            # Move the left pointer to the end of the current range
            l = r + 1
            # Update the right pointer to the maximum jump distance found
            r = maxJump
            # Increment the number of jumps
            ans += 1
        # Return the total number of jumps
        return ans
        