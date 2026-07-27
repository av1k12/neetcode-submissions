class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in s_seen:
                s_seen[s[i]] = s_seen[s[i]] + 1
            else:
                s_seen[s[i]] = 0

            if t[i] in t_seen:
                t_seen[t[i]] = t_seen[t[i]] + 1
            else:
                t_seen[t[i]] = 0
        
        if t_seen == s_seen:
            return True
        return False
        