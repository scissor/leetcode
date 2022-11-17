#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    # Offset 技法
    # DIR = [0, 1, 0, -1, 0]
    # for i in range(4):
    #    nx, ny = x + DIR[i], y + DIR[i + 1]
    # => (0,1), (1,0), (0,-1), (-1,0)
    
    # BFS：不用 visit，初始化未走過的為 -1，Code較簡潔
    # 但需要先判斷邊界，所以可能會較使用 set 還慢
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        explore = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    explore.append((i, j))
                else:
                    mat[i][j] = -1

        offsets = [(1,0), (-1,0), (0,1), (0,-1)]
        while explore:
            x, y = explore.pop(0)

            for ox, oy in offsets:
                nx, ny = x + ox, y + oy
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] < 0:
                    mat[nx][ny] = mat[x][y] + 1
                    explore.append((nx, ny))
        return mat
    
    
    # BFS：紀錄 visit 和 explore
    def updateMatrix_2(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        explore = []
        visit = set()
        offsets = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    explore.append((i, j))
                    visit.add((i, j))

        while explore:
            x, y = explore.pop(0)

            for ox, oy in offsets:
                nx, ny = x + ox, y + oy
                walk = (nx, ny)
                if walk in visit:
                    continue

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                mat[nx][ny] = mat[x][y] + 1
                explore.append(walk)
                visit.add(walk)
        return mat


    # RecursionError: maximum recursion depth exceeded in comparison
    def updateMatrix_1(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        def dp(mat, i, j):
            cost = mat[i][j]
            if i - 1 > 0:
                cost = min(cost, dp(mat, i-1, j))
            if i + 1 < m:
                cost = min(cost, dp(mat, i+1, j))
            if j - 1 > 0:
                cost = min(cost, dp(mat, i, j-1))
            if j + 1 < n:
                cost = min(cost, dp(mat, i, j+1))
            return cost

        for i in range(m):
            for j in range(n):
                mat[i,j] = dp(mat, i, j)
                
        return mat
# @lc code=end

