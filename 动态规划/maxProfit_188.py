'''
188. 买卖股票的最佳时机 IV
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 交易数受到限制，交易数影响状态
        n = len(prices)
        if n == 0 or n == 1: return 0
        K = k
        def max_infi(prices):
            n = len(prices)
            if n == 0 or n == 1: return 0
            dp_0, dp_1 =  0, -prices[0] # 前一天不持有股票的最大获利/持有股票的最大获利
            for i in range(1, n):
                i_not_have = max(dp_1 + prices[i], dp_0) # 第i天不持有股票的最大获利：两种情况取最大 
                                                        # (1) 前一天不持有 （2）前一天持有，第i天卖出
                i_have = b = max(dp_1, dp_0 - prices[i]) # 第i天持有股票的最大获利: 两种情况取最大 
                                                    # (1) 前一天持有 （2）前一天不持有，第i天买进（因为买进卖出次数不受限制，所以这里使用dp_0 ！ 而不是121题中的0， 仅仅跟121题有这点区别！）
                dp_0, dp_1 = i_not_have, i_have
            return i_not_have
        if K > n // 2: return max_infi(prices)
        # create 三维 dp list
        dp = []
        for i in range(n):
            dp_item = [[float('-inf')] * 2 for i in range(K + 1)]
            dp.append(dp_item)
        # 初始化边界
        for k in range(K + 1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        for i in range(n):
            dp[i][0][0], dp[i][0][1] = 0, 0 
        
        # 状态转移
        for i in range(1, n):
            for k in range(1, K + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][K][0]