class Solution:
    def solveNQueens(self, n):
        self.result = []
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.n = n
        self.solve(0)
        return self.result
    
    def solve(self, row):
        if row == self.n:
            self.result.append(self.constructBoard())
            return
        
        for col in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col] = 'Q'
                self.solve(row + 1)
                self.board[row][col] = '.'
    
    def isSafe(self, row, col):
        # Check column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def constructBoard(self):
        return [''.join(row) for row in self.board]