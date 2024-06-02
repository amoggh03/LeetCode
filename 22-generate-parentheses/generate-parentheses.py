class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, open, close, n):
            if len(cur) == 2 * n:
                if open == close:
                    res.append(cur)
                return

            if open < n:
                dfs(cur + "(", open + 1, close, n)
            if open > close:
                dfs(cur + ")", open, close + 1, n)

        dfs("", 0, 0, n)
        return res