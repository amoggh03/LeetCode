class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        x = ['(', '{', '[']
        y = [')', '}', ']']
        for i in range(len(s)):
            word = s[i]
            check.append(word)
            if len(check) > 1 and check[-1] in y and check[-2] in x:
                # Check if the last two elements form a valid pair
                if x.index(check[-2]) == y.index(check[-1]):
                    # Remove the opening bracket
                    check.pop(-2)
                    # Remove the closing bracket
                    check.pop()
                else:
                    # Invalid pair, return False
                    return False
        # If the check list is empty at the end, it means all brackets are matched.
        return len(check) == 0

