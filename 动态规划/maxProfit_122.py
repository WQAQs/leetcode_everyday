# '''122. 买卖股票的最佳时机 II
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
# ‘’‘

class Solution:
     # 动态规划
    def maxProfit(self, prices: List[int]) -> int:
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