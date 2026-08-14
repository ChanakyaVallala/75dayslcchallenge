class Solution(object):
    def bfs(self,q,board):
        ROWS = len(board)
        COLS = len(board[0])
        dns = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in dns:
                i = r + dr
                j = c + dc
                # strictly out of bounds mean one O value is in the boundaries
                if(i<0 or i==ROWS or j<0 or j==COLS or board[i][j]=="T"):
                    continue
                if(board[i][j]=="O"):
                    board[i][j]="T"
                    q.append((i,j))
        return     


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from collections import deque
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        q = deque()
        for i in range(ROWS):
            if(board[i][0]=="O"):
                q.append((i,0))
                board[i][0]="T"
                self.bfs(q,board)
            if(board[i][COLS-1]=="O"):
                q.append((i,COLS-1))    
                board[i][COLS-1]="T"
                self.bfs(q,board)
        for j in range(COLS):
            if(board[0][j]=="O"):
                q.append((0,j))
                board[0][j]="T"
                self.bfs(q,board)
            if(board[ROWS-1][j]=="O"):
                q.append((ROWS-1,j))
                board[ROWS-1][j]="T"
                self.bfs(q,board)  
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"
        
        return
        
        