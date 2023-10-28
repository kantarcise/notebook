"""
Given an m x n grid of characters board and a string 
word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent 
cells, where adjacent cells are horizontally or 
vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Takeaway:

we have to brute force
not an efficient solition here.
look at every single position 
check every neighbor

We will use dfs and recursive backtracking

Even before we get to dfs, 
we can check if all letters in the word 
are actually in the board 

for writing the dfs 

do not forget about all the cases in your question

end of the word
out of bounds
character not matching
position already in path

GO TO NEXT
row either + or - 
OR
column either + or -

time complexity

o(n * m * dfs) - dfs is (4 * len(word))


"""

class Solution:
    def exist(self, board: "list[list[str]]", word: str) -> bool:
        # we have to brute force
        # not an efficient solition here.
        # look at every single position 
        # check every neighbor
        # 
        # We will use dfs and recursive backtracking

        ROWS, COLS = len(board), len(board[0])

        # because we want unique characters
        path = set() 

        # can this make a difference?
        # just slap it in there
        unique_chars = set(word)
        for elem in unique_chars:
            if elem not in [element for row in board for element in row]:
                return False

        # position of the board, and i - current character 
        # location in the target that we are looking for position
        def dfs(r, c, i):
            if i == len(word):
                # we finished, found the word
                return True

            # if we are out of bounds
            # if the character does not match
            # or the position is already in our path
            if (r >= ROWS or c >= COLS or 
                r < 0 or c < 0 or
                word[i] != board[r][c] or
                (r, c) in path): 
                return False

            # we FOUND THE CHARACTER
            path.add((r,c))

            # GO TO NEXT
            # r + - 
            # OR
            # c + -
            res = (dfs(r + 1, c, i + 1) or 
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or
                  dfs(r, c - 1, i + 1))

            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): 
                    return True

        return False


# another solution from a fellow programmer
from collections import defaultdict, Counter

class SecondSolution:
    def exist(self, board: "list[list[str]]", word: str) -> bool:
        # same approach here
        def backtrack(board, word, index, r, c):
            if index == len(word):
                return True

            if (r >= 0 and r < len(board) and 
                c >= 0 and c < len(board[0]) and 
                board[r][c] and 
                board[r][c] == word[index]): 

                currLetter = board[r][c]
                board[r][c] = None
                result = (backtrack(board, word, index+1, r+1, c) 
                    or backtrack(board, word, index+1, r-1, c) 
                    or backtrack(board, word, index+1, r, c+1) 
                    or backtrack(board, word, index+1, r, c-1))
                board[r][c] = currLetter

                return result
            
        # Count number of letters in board and store it in a dictionary
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(board, word, 0, r, c):
                    return True