class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) == 0:
            return ranges

        start = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                ranges.append(self.format_range(start, nums[i]))
                start = nums[i + 1]
        ranges.append(self.format_range(start, nums[-1]))  # Append last range
        return ranges

    def format_range(self, start: int, end: int) -> str:
        if start == end:
            return str(start)  # Single element range
        else:
            return f"{start}->{end}"  # Range with start and end values
