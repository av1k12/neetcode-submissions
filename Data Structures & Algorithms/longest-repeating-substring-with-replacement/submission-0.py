class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = {}
        length = 0
        freq_char = 0

        for r in range(len(s)):
            new_char = s[r]
            chars[new_char] = chars.get(new_char, 0) + 1

            win_size = r - l + 1
            freq_char = max(freq_char, chars[new_char])

            while win_size - freq_char > k:
                leaving = s[l]
                chars[leaving] -= 1
                l += 1

                win_size = r - l + 1
            length = max(win_size, length)
        return length