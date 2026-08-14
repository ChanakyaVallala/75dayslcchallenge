from collections import deque

class Solution:
    def solve(self, board):
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        q = deque()
        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r, 0))
                board[r][0] = '#'

            if board[r][cols - 1] == 'O':
                q.append((r, cols - 1))
                board[r][cols - 1] = '#'

        for c in range(cols):
            if board[0][c] == 'O':
                q.append((0, c))
                board[0][c] = '#'
            if board[rows - 1][c] == 'O':
                q.append((rows - 1, c))
                board[rows - 1][c] = '#'
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] == 'O'):
                    board[nr][nc] = '#'
                    q.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'