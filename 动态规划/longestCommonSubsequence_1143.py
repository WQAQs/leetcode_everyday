# 1143. 最长公共子序列
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

# 若这两个字符串没有公共子序列，则返回 0。


# 示例 1:

# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 示例 2:



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # 1. 状态定义，dp数组初始化
        #    dp[i][j]定义为text1[0, i)与text2[0, j)的最长公共序列 !
        dp = [[0] * (m + 1) for i in range(n + 1)]
        # 2. 边界值
        for j in range(m + 1):
            dp[0][j] = 0
        for i in range(n + 1):
            dp[i][0] = 0
        # 3. 遍历状态并填充——根据状态转移方程填充
        for i in range(1, n + 1):  #【状态i】的所有可能值：i～[1, n]
            for j in range(1, m + 1): #【状态j】的所有可能值：j～[1, m]
                # 【不同的选择】：
                if text2[i - 1] == text1[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
                
