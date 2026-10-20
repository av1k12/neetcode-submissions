class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEOW = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEOW = True        

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.isEOW
        return dfs(0, self.root)
