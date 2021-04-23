# 322. 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 你可以认为每种硬币的数量是无限的。

 

# 示例 1：

# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
# 示例 2：

# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
 

# 提示：

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. 定义状态 2.初始化
        # dp[i] 为凑出零钱i所需要的最小硬币个数
        dp = [sys.maxsize for i in range(amount + 1)]
        # 3. 边界值
        dp[0] = 0
        for i in range(amount + 1): # 4.填充dp数组 状态转移
            for c in coins: # 可以选择的不同硬币 + 之前的状态
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1) # 状态转移
        return dp[amount] if dp[amount] != sys.maxsize else -1 # 5. 确定最终返回值

