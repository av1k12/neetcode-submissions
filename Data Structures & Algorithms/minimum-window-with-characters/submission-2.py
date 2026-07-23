class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""

        #requirements for window to be valid
        count = {}
        for i in t:
            count[i] = count.get(i, 0) + 1
        min_unique_chars = len(count)

        #window stuff
        win_count = {}
        satisfied = 0 #satisfied gotta equal min_unique_chars
        l = 0
        min_size = float("inf")
        ans_indices = (-1, -1)

        for r in range(len(s)):
            cur_char = s[r]

            if cur_char in count:
                win_count[cur_char] = win_count.get(cur_char, 0) + 1
                if win_count[cur_char] == count[cur_char]:
                    satisfied += 1
            
            while satisfied == min_unique_chars:
                win_size = r-l+1
                if win_size < min_size:
                    min_size = win_size
                    ans_indices = (l,r)

                leaving_char = s[l]
                if leaving_char in count:
                    if win_count[leaving_char] == count[leaving_char]:
                        satisfied -= 1
                    win_count[leaving_char] -= 1
                l += 1
        start, end = ans_indices
        return s[start:end+1] if min_size != float('inf') else ""


