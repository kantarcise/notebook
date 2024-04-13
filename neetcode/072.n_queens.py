"""
The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to 
the n-queens puzzle. 

You may return the answer in any order.

Each solution contains a distinct board configuration of 
the n-queens' placement, where 'Q' and '.' both indicate 
a queen and an empty space, respectively.

Example 1:

    Input: n = 4
    
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    
    Explanation: 
        There exist two distinct solutions to 
            the 4-queens puzzle as shown above

Example 2:

    Input: n = 1
    
    Output: [["Q"]]

Constraints:

    1 <= n <= 9

Takeaway:


    Backtracking the positions of the queens, but since 
        queens can move horizontally vertically and 
        diagonally, we can’t put two queens together 
        in the same row (because they move horizontally 
        so would attack each other) and also can’t put 
        them in same column or diagonal. So when 
        backtracking, we place queen in a position in 
        row and make recursive call to place the other 
        in next row and keep track of:

    Column that queen was placed in
        Both diagonals of the queen (YES there are 
        TWO diagonals that the queen can move in, 
        positive slope and negative slope, so need 
        to keep track of both)
"""

class Solution:

    def solveNQueens__(self, n: int) -> "list[list[str]]":
        # my first approach
        # did NOT work
        
        # how can we decide where to put the queens.
        # ?
        # it is kinda like a decision tree.
        # each row has 1 queen at most
        # queens also cannot be in same column
        # the indexes has to be at least 2 apart.
        
        result = []
        board = [ ["." * n] for elem in range(n) ]
        
        def backtrack(i, queens_in_rows):
            if len(queens_in_rows) == n:
                # will fix this
                result.append("path")
                return

            # there has to be some condition here..            
            backtrack(i + 1, queens_in_rows)
        
        if n == 1:
            return [["Q"]]
        
        backtrack(0, {})
        return result

    def solveNQueens_(self, n: int) -> "list[list[str]]":
        # with EXPERT help, works

        def is_valid(board, row, col):
            # Check the current column for a queen in any of the rows above
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check the upper-left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # Check the upper-right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtrack(row):
            if row == n:
                # All queens are successfully placed, add the current board configuration
                result.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_valid(board, row, col):
                    # Place the queen
                    board[row][col] = 'Q'
                    # Recur to the next row
                    backtrack(row + 1)
                    # Backtrack by removing the queen
                    board[row][col] = '.'

        # Initialize an empty chessboard
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        backtrack(0)  # Start from the first row
        return result

    def solveNQueens(self, n: int) -> "list[list[str]]":
        # there is a slope 1 and slope -1
        # diagonals, 2 queens cannot be on same diagonals

        col = set()
        positive_diagonal = set() # r + c - this value 
        # will be same on the diagonal
        negative_diagonal = set() # r - c - this value 
        # will be same on the diagonal

        res = []

        board = [["." ] * n  for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in positive_diagonal \
                    or (r - c) in negative_diagonal:
                    continue

                col.add(c)
                positive_diagonal.add(r + c)
                negative_diagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
