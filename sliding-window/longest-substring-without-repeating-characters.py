class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        current_substring = []
        
        for i in range(len(s)):
            if s[i] not in current_substring:
                current_substring.append(s[i])
            else:
                longest_length = max(longest_length, len(current_substring))
                
                while current_substring[0] != s[i]:
                    current_substring.pop(0)
                current_substring.pop(0) 
                current_substring.append(s[i]) 
            
        longest_length = max(longest_length, len(current_substring))  
        
        return longest_length
