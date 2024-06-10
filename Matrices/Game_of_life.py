class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Condition for live cell:
        # 2 or 3 neighbours -> Live else dead
        # Condition for dead cell:
        # 3 neighbours -> Live else dead
        # Similar to the truth table
        # Original | New | State
        #     0    |  0  |  0
        #     1    |  0  |  1
        #     0    |  1  |  2
        #     1    |  1  |  3

        Rows = len(board)
        Cols = len(board[0])

        # Count neighbours helper function
        def CountNeighbours(r, c):
            # We need to check a total of 8 neighbours
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    # The first bracket checks if it is the same element
                    # The second bracket checks for the lower bound
                    # The third bracket checks for the upper bound
                    if ((i == r and j == c) or (i < 0 or j < 0) or (i == Rows or j == Cols)):
                        continue
                    # Implies that the cell is live. Check the truth table above
                    if board[i][j] in {1, 3}:
                        nei += 1
            return nei

        # Building the new matrix but with some temp values
        # Original to state conversion
        for r in range(Rows):
            for c in range(Cols):
                nei = CountNeighbours(r, c)
                if board[r][c] == 1:
                    if nei in {2, 3}:
                        board[r][c] = 3
                    else:
                        board[r][c] = 1
                else:
                    if nei == 3:
                        board[r][c] = 2
                    else:
                        board[r][c] = 0

        # Building the final matrix after conversion
        # State to new conversion
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] in {2, 3}:
                    board[r][c] = 1

                else:
                    board[r][c] = 0
