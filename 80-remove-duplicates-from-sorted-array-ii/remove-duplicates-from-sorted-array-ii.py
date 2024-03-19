from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=Counter(nums)
        arr=[]
        for count.key,count.value in count.items():
            if count.value<3:
                for j in range(count.value):
                    arr.append(count.key)
            else:
                for k in range(2):
                    arr.append(count.key)
            for i in range(len(arr)):
                nums[i]=arr[i]                    
        return len(arr)