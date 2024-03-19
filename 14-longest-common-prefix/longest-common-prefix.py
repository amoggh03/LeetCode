class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first= strs[0]
       
        last= strs[-1]
        mini= min(len(first), len(last))
        for i in range(mini):
            if first[i]!=last[i]:
                return last[:i]
        return last[:mini]    


        