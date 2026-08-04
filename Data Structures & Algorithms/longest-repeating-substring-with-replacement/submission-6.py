class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        cur_max = 0

        for r in range(len(s)):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1
            
            # If (window_length - max_frequency) > k, window is invalid
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            cur_max = max(cur_max, r - l + 1)

        return cur_max