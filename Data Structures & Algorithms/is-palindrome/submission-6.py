class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and s[l].isalnum() == False:
                print(s[l])
                l+=1
            while r > l and s[r].isalnum() == False:
                print(s[r])
                r -=1
            if s[l].lower() != s[r].lower():
                print(s[l], "  ", s[r])
                return False
            l += 1
            r -= 1
        return True
        