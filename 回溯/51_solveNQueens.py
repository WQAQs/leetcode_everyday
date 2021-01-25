# 51. N 皇后
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

# 示例 1：输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：

# 输入：n = 1
# 输出：[["Q"]]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def myFormat(m, n):
            temp = ""
            for i in range(n):
                if i == m:
                    temp += "Q"
                else:
                    temp += "."
            return temp
        
        def isValid(col_i, path):
            for row_i in range(len(path)):
                temp = path[row_i]
                offset = len(path) - row_i
                if temp[col_i] == "Q": # garantee not in the same column
                    return False
                if col_i - offset >= 0 and temp[col_i - offset] == "Q": # garantee not in the same diagonal 0
                    return False
                if col_i + offset < len(temp) and temp[col_i + offset] == "Q": # garantee not in the same diagonal 1
                    return False
            return True

        def backtrace(n, path):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if isValid(i, path):
                    path.append(myFormat(i, n))
                    backtrace(n, path)
                    path.pop()
        backtrace(n, [])
        return res