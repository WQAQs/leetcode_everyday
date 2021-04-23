# 516. 最长回文子序列
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

 

# 示例 1:
# 输入:

# "bbbab"
# 输出:

# 4
# 一个可能的最长回文子序列为 "bbbb"。

# 示例 2:
# 输入:

# "cbbd"
# 输出:

# 2
# 一个可能的最长回文子序列为 "bb"。


class Solution:
    # 动态规划
    # 找到状态和选择 -> 明确 dp 数组/函数的定义 -> 寻找状态之间的关系。
    # dp 数组要便于使用归纳法，使得可以由已经计算出来的dp状态计算dp[n]
    # dp[i][j]定义为s[i : j]的最长回文子序列长度
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * len(s) for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else: 
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]
        
        