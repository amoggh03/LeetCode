class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while n != 1 and n not in seen:
            seen.add(n)
            digits = [int(digit) for digit in str(n)]
            summ = sum(digit * digit for digit in digits)
            n = summ
        return n == 1