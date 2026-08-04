class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        maxWin = 0
        window = set()

        

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
            else:
                if (r-l) > maxWin:
                    maxWin = r-l
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
            r += 1
        if (r-l) > maxWin:
            maxWin = r-l
        return maxWin
