class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        maxlen = 0
        r = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            cur = r - l + 1
            if cur > maxlen:
                maxlen = cur
            r += 1
        return maxlen


