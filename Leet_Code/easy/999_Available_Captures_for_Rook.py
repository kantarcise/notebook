"""
On an 8 x 8 chessboard, there is exactly one 
white rook 'R' and some number of white 
bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four 
cardinal directions (north, east, south, or west), 
then moves in that direction until it chooses to stop, 
reaches the edge of the board, captures a black pawn, 
or is blocked by a white bishop. 

A rook is considered attacking a pawn if the rook 
can capture the pawn on the rook's turn. 

The number of available captures for the white rook 
is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

Example 1:


  Input: board = [[".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".","R",".",".",".","p"],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."]]
    Output: 3

    Explanation: In this example, the rook is attacking all the pawns.

Example 2:

  Input: board = [[".",".",".",".",".",".",".","."],
                  [".","p","p","p","p","p",".","."],
                  [".","p","p","B","p","p",".","."],
                  [".","p","B","R","B","p",".","."],
                  [".","p","p","B","p","p",".","."],
                  [".","p","p","p","p","p",".","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","."]]

    Output: 0

    Explanation: 
    
        The bishops are blocking the rook from attacking any of the pawns.


Example 3:

  Input: board = [[".",".",".",".",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  ["p","p",".","R",".","p","B","."],
                  [".",".",".",".",".",".",".","."],
                  [".",".",".","B",".",".",".","."],
                  [".",".",".","p",".",".",".","."],
                  [".",".",".",".",".",".",".","."]]

    Output: 3

    Explanation: 
    The rook is attacking the pawns at positions b5, d6, and f5.
 
Constraints:

    board.length == 8

    board[i].length == 8

    board[i][j] is either 'R', '.', 'B', or 'p'

    There is exactly one cell with board[i][j] == 'R'

Takeaway:

    checking rows and columns.

"""
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # only one white rook
        # white bishops, black pawns
        
        # find R in the board
        # see all pawns in horizontal and vertical
        # look out for black bishops!
        
        r, c = 0, 0
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    r, c = i, j
                    break
                    
        # now we know
        # 4 different possibilities

        count = 0
        
        # in the column
        # from top to middle!
        for i in range(r-1, -1, -1):
            if board[i][c] == 'p':
                count+=1
                break
            elif board[i][c] == 'B':
                break
        
        # in the column
        # from rook to bottom
        for i in range(r+1, 8):
            if board[i][c] == 'p':
                count+=1
                break
            elif board[i][c] == 'B':
                break
    
        # in the row
        # from rook to left
        for i in range(c-1, -1, -1):
            if board[r][i] == 'p':
                count+=1
                break
            elif board[r][i] == 'B':
                break
        
        # in the row
        # from rook to right
        for i in range(c+1, 8):
            if board[r][i] == 'p':
                count+=1
                break
            elif board[r][i] == 'B':
                break
                
        return count
