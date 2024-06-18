from collections import deque


class Solution:
    def snakesAndLadders(self, board: 'List[List[int]]') -> int:
        length = len(board)
        board.reverse()

        def inttoPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            # If it is an odd row we need to make the switch
            if r % 2:
                c = length - 1 - c
            return [r, c]

        temp_q = deque()  # It will store the sq pos and the number of moves
        visit = set()
        temp_q.append((1, 0))
        visit.add(1)

        while temp_q:
            sq_no, moves = temp_q.popleft()
            for i in range(1, 7):
                new_sq_no = sq_no + i
                r, c = inttoPos(new_sq_no)

                if board[r][c] != -1:
                    new_sq_no = board[r][c]

                if new_sq_no == length * length:
                    return moves + 1

                if new_sq_no not in visit:
                    temp_q.append((new_sq_no, moves + 1))
                    visit.add(new_sq_no)

        return -1







