class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(s.split())
        final_text = "".join(c for c in text if c.isalnum()).lower()
        mid = int(len(final_text)/2)
        print(mid)
        print(final_text)

        index_first = 0
        index_last = -1
        for i in range(len(text)):
            if index_first != mid:
                if final_text[index_first] != final_text[index_last]:
                    return False
            else:
                return True
            print(final_text[index_first] + " " + final_text[index_last])
            index_first += 1
            index_last -= 1
        
        return True