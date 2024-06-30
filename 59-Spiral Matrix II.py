class Solution(object):
    def generateMatrix(self, n):
        top, bottom, left, right = 0, n-1, 0, n - 1
        val = 1
        arr = [[0] * n for _ in range(n)]

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                arr[top][j] = val
                val += 1
            top += 1

            for i in range(top, bottom + 1):
                arr[i][right] = val
                val += 1
            right -= 1

            for j in range(right, left - 1, -1):
                arr[bottom][j] = val
                val += 1
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                arr[i][left] = val
                val += 1
            left += 1
        return arr