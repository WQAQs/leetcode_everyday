# 875. 爱吃香蕉的珂珂
# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

# 珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

# 返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

# 示例 1：

# 输入: piles = [3,6,7,11], H = 8
# 输出: 4
# 示例 2：

# 输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
# 示例 3：

# 输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
 

# 提示：

# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9

### 思路解析：https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/shou-ba-shou-shua-shu-zu-ti-mu/koko-tou-xiang-jiao

import heapq
class Solution:

    ## 理解题目： 
    ## （1）题目要求的是啥？
    # 提炼要求，就是要计算H小时内要吃完香蕉的最小速度

    ## （2）限制条件？
    # 每个小时只能吃一堆，若一堆的香蕉数目小于speed， 1小时内就能把选的这堆吃完，否则剩下的下一个小时再吃

    ## （3）怎么计算能否吃完？
    # 计算吃完所有香蕉的时间t，若 t <= H , 则能按要求吃完，否则不能
    ## 怎么计算吃完所有香蕉的时间t？
    # 计算吃完每一堆香蕉的时间，然后相加得到总时间

## 1. 暴力解法
    ## O(n^2) ，最大只能处理n=1e4的数据规模
    ## 吃香蕉最小速度1，最大速度max(piles),从小到大遍历[0, max(piles)]，第一个找到能吃完香蕉的速度（即左边界）即为结果
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for speed in range(1, heapq.nlargest(1, piles)[0] + 1): # 注意！！ heapq.nlargest(1, piles)返回的是一个list
            if can_finish(speed, piles):
                return speed
        return speed

## 2. 二分查找
    ## 把1中暴力解法的for循环线性遍历改为二分查找
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed, piles):
            time = 0
            for n in piles:
                time += n // speed + (1 if n % speed > 0 else 0)
            return time <= h
        left, right = 1, heapq.nlargest(1, piles)[0] + 1 # 搜索范围[left, right)
        while left < right:   # left == right 搜索范围内无值，退出循环
            mid = left + (right - left) // 2
            if can_finish(mid, piles):
                right = mid   # 收缩右侧边界到符合要求的点（有效点）
            else: 
                left = mid + 1  # 不断右移，寻找左边界点
        return left
        