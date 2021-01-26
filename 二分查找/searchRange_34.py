'''
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 寻找左边界/右边界
        def find_left(nums, target, flag):
            n = len(nums)
            if n == 0: return -1
            # 考察的窗口范围是： nums[left, right)
            left, right = 0, n # 所以right的初始值为n
            # 所以while循环结束的条件是left == right, 即考察的窗口变为了：nums[left, left)，窗口内没有元素了
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1 
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] == target:
                    if flag: right = mid # 如果是寻找左边界，收缩右边
                    else: left = mid + 1 # 如果是寻找右边界，收缩左边
            if flag:
                if left == n: return -1 # nums数组中的每一项都比target小
                return left if nums[left] == target else -1 # 如果二分搜索找到了target就返回左边界，否则返回-1
            else:
                if right == 0: return -1 # nums数组中的每一项都比target大
                return  left - 1 if nums[left - 1] == target else -1 # 如果二分搜索找到了target就返回右边界，否则返回-1
                                                                     # 因为代码 53 行， 知道应该判断的是nums[left - 1]是否等于target

        left, right = find_left(nums, target, True), find_left(nums, target, False)
        return [left, right]