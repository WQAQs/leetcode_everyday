# 53. 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


# 示例 1：

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0] # dp[i]定义为以nums[i]结尾的最大子序和
        res = 0
        for num in range(nums):
            dp = max(dp + num, num) # dp[i]只和dp[i - 1]有关，两种选择
            res = max(res, dp) # 记录全局最大值
        return res # 返回全局最大