# 121. 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

# 示例 1：

# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：

# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

# 提示：

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    # 方法1. 动态规划
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1: return 0
        
        # 1. 定义状态，dp_0, dp_1分别是当天不持有股票的最大获利、持有股票的最大获利

        dp_0, dp_1 =  0, -prices[0] # 当天不持有股票的最大获利/持有股票的最大获利
        for i in range(1, n):
            i_not_have = max(dp_1 + prices[i], dp_0) # 第i天不持有股票的最大获利：两种情况取最大 
                                                     # (1) 前一天不持有 （2）前一天持有，第i天卖出
            i_have = b = max(dp_1, - prices[i]) # 第i天持有股票的最大获利: 两种情况取最大 
                                                # (1) 前一天持有 （2）前一天不持有，第i天买进（因为总共只能买进卖出1次，所以前一天的利润一定是为0！！！这里不能使用dp_0）
            dp_0, dp_1 = i_not_have, i_have

    # 方法2. 在【历史最低点】买入
    # 在【历史最低点】后找到prices[i] - min_price的最大值即为最大利润
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1: return 0
        min_price, max_profit = float('inf'), float('-inf')
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit