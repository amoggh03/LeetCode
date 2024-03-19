class Solution(object):
    def isPalindrome(self, s):
        lower = s.lower()
        words = lower.split()
        s_without_punctuation = ''.join(char for char in lower if char.isalnum())
        print(s_without_punctuation)
        if s_without_punctuation==s_without_punctuation[::-1]:
            return True
        else:
            return False    






        