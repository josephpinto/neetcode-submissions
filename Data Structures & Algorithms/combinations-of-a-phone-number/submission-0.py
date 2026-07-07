class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            next_digit = digits[len(curr)]

            for letter in digitToChar[next_digit]:
                curr += letter
                dfs(curr)
                curr = curr[:-1]
        dfs("")
        return res