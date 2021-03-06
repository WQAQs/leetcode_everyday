# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

# 示例 1：

# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：

# class Solution {
#     public int rob(int[] nums) {
#         int pre = 0, cur = 0, tmp;
#         for(int num : nums) {
#             tmp = cur;
#             cur = Math.max(pre + num, cur);
#             pre = tmp;
#         }
#         return cur;
#     }
# }



class Solution:
    def rob(self, nums: List[int]) -> int:
        # （1）明确状态和选择：可以选择打劫/不打劫，状态：不同的房屋索引
        # （2）选择与状态转移：打劫当前房屋，则下一个房屋不能打劫，只能从下下个房屋开始打劫；
        #                   不打劫当前房屋，则下一个房屋可以打劫
        # （3）明确重叠子问题和最优子结构，dp数组定义为： 
        #      dp[i]为nums[i, ... , len(nums) - 1]房屋区域能盗窃的最大金额
        
        # 1. 没有状态压缩，直接使用一个一维dp数组
        n = len(nums)
        if n == 0: return 0
        dp = [0 for i in range(n + 1)]
        dp[n], dp[n - 1] = 0, nums[-1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 2] + nums[i], dp[i + 1]) # 抢/不抢当前房屋两种选择
        return dp[0]

        # 2. 压缩状态： 因为只需要前两个状态的结果，只保存前两个结果就可以
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        dp_1 , dp_2 = 0, nums[-1]
        for i in range(n - 2, -1, -1):
            dp = max(nums[i] + dp_1, dp_2)
            dp_1, dp_2 = dp_2, dp
        return dp



