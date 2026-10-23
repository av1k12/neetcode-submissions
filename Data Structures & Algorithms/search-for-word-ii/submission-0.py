class TrieNode:
    def __init__(self):
        # Maps a character to the next TrieNode: {'a': TrieNode, ...}
        self.children = {}
        # Stores the complete word string once reaching its last character (e.g., "rat")
        # If no word ends here, it remains None
        self.word = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # -------------------------------------------------------------
        # STEP 1: Build the Trie with all target words
        # -------------------------------------------------------------
        root = TrieNode()
        for w in words:
            curr = root
            for ch in w:
                # If character path doesn't exist, create a new branch node
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            # Store the word directly on the leaf node to avoid rebuilding strings during DFS
            curr.word = w

        rows, cols = len(board), len(board[0])
        res = []

        # -------------------------------------------------------------
        # STEP 2: Depth-First Search with Backtracking and Trie Pruning
        # -------------------------------------------------------------
        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            # Advance to the corresponding node in the Trie
            curr_node = parent_node.children[char]

            # If this node completes a valid word, record it in the results
            if curr_node.word:
                res.append(curr_node.word)
                # Set to None immediately so the same word isn't added again via a different path
                curr_node.word = None

            # Temporarily mark the cell as visited so this branch cannot reuse it
            board[r][c] = "#"

            # Check all 4 adjacent directions: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check grid boundaries
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Only recurse if the neighbor's character is a valid next step in the Trie
                    if board[nr][nc] in curr_node.children:
                        dfs(nr, nc, curr_node)

            # Backtrack: Restore original board character so other starting paths can use this tile
            board[r][c] = char

            # Trie Pruning: If this node has no children left, it is an exhausted dead end.
            # Remove it from the parent so future scans never waste time traversing down here.
            if not curr_node.children:
                parent_node.children.pop(char)

        # -------------------------------------------------------------
        # STEP 3: Iterate through the grid and start DFS where valid
        # -------------------------------------------------------------
        for r in range(rows):
            for c in range(cols):
                # Only initiate DFS if the cell's letter can actually start a word in the Trie
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res