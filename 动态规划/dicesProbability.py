from typing import List
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # 1. 定义状态：dp[i][j]为i个骰子总和为j的组合数
        mins, maxs = 1, 6*n
        # 2. 初始化二维dp数组，边界值
        dp = [[0] * (6*n + 1) for i in range(n + 1)]
        for j in range(1, 1*6+1):
            dp[1][j] = 1
        # 3. 遍历赋值dp数组 —— 状态转移
        for i in range(2, n + 1):  # （1）【骰子i的状态】遍历：i ~ [2, n] 
            for j in range(i, i * 6 + 1): # （2）【骰子和j的状态】遍历：j ～ [i, i*6]
                #（3）【不同的选择】：当前，第i个骰子可能点数: num ～[1, 6] 
                #     ——》》状态dp[i][j]由dp[i - 1][不同选择对应的前一步的j状态]得到
                for num in range(1, 7): 
                    if j > num : dp[i][j] += dp[i - 1][j - num] # 状态转移
        def func(sn):
            return sn / sum(dp[n])
        sumn = sum(dp[n])
        return list(map(func, dp[n]))[n:]

so = Solution()
so.dicesProbability(2)

