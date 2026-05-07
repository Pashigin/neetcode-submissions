class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        res = []

        for char in s:
            if char in brackets:
                if res and brackets[char] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)

        return len(res) == 0