# 46. 全排列
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(nums, path):
            if len(path) == len(nums):
                res.append(path[:]) # attention！ use path[:] instead of path
                return 
            for value in nums:
                if value not in path:
                    path.append(value)
                    backtrace(nums, path)
                    path.pop()
        backtrace(nums, [])
        return res