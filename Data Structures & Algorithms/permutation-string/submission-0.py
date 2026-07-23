class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        left = 0
        right = k - 1
        
        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1
        
        window_counts = {}
        for i in range(k):
            window_counts[s2[i]] = window_counts.get(s2[i], 0) + 1
        
        if window_counts == s1_counts:
            return True
        
        while right < len(s2) - 1:
            outgoing = s2[left]
            window_counts[outgoing] -= 1
            if window_counts[outgoing] == 0:
                del window_counts[outgoing]
            left += 1
            right += 1
            incoming = s2[right]
            window_counts[incoming] = window_counts.get(incoming, 0) + 1

            if window_counts == s1_counts:
                return True
        return False


        