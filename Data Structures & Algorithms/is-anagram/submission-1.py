class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur_s = {}
        occur_t = {}

        for ch in s:
            if ch in occur_s:
                occur_s[ch] += 1
            else:
                occur_s[ch] = 1

        for ch in t:
            if ch in occur_t:
                occur_t[ch] += 1
            else:
                occur_t[ch] = 1

        if len(occur_t) != len(occur_s):
            return False

        for key, value in occur_s.items():
            if key not in occur_t or value != occur_t[key]:
                return False
        
        return True
