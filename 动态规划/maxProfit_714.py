'''
714. 买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0 or n == 1: return 0
        dp_0, dp_1 =  0, -prices[0] - fee # 前一天不持有股票的最大获利/持有股票的最大获利(注意初始状态持有也是有手续费的)
        for i in range(1, n):
            i_not_have = max(dp_1 + prices[i], dp_0) # 第i天不持有股票的最大获利：两种情况取最大 
                                                     # (1) 前一天不持有 （2）前一天持有，第i天卖出
            i_have = b = max(dp_1, dp_0 - prices[i] - fee) # 第i天持有股票的最大获利: 两种情况取最大 
                                                # (1) 前一天持有 （2）前一天不持有，第i天买进（因为买进卖出次数不受限制，所以这里使用dp_0 ！ 因为交易有手续费，所以统一在买入的时候交手续费）
            dp_0, dp_1 = i_not_have, i_have
        return i_not_have