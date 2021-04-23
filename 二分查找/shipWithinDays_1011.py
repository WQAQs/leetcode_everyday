# 1011. 在 D 天内送达包裹的能力
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

# 示例 1：

# 输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# 输出：15
# 解释：
# 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
# 第 1 天：1, 2, 3, 4, 5
# 第 2 天：6, 7
# 第 3 天：8
# 第 4 天：9
# 第 5 天：10

# 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
# 示例 2：

# 输入：weights = [3,2,2,4,1,4], D = 3
# 输出：6
# 解释：
# 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
# 第 1 天：3, 2
# 第 2 天：2, 4
# 第 3 天：1, 4
# 示例 3：

# 输入：weights = [1,2,3,1,1], D = 4
# 输出：3
# 解释：
# 第 1 天：1
# 第 2 天：2
# 第 3 天：3
# 第 4 天：1, 1
 

# 提示：

# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500

## 思路：
# 类似猴子吃香蕉，（1）先依据暴力解法，确定最低运力的搜索范围：[max(weights),sum(weights)]；
# （2）使用二分搜索找到最低运力（即左边界）
# 注意限制条件： 因为包裹是不可分的所以最小值为 max(weights)
import heapq
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can_finish(cap, weights, D):
            i = 0
            for t in range(D): 
                t_cap = cap # 每一天的运量t_cap想装满 
                while (t_cap - weights[i]) >=0: # 还能放下货物i，才i++
                    t_cap -= weights[i] # 今天的运量
                    i += 1
                    if i >= len(weights): # 注意！ 判断i有没有超过范围，一定要放这里
                        return True
            return False 
        min_s = heapq.nlargest(1, weights)[0] # 用堆排序计算max(weights)
        # 内置求和函数sum(iterable, start = 0) 
        # Return the sum of a 'start' value (default: 0) plus an iterable of numbers
        max_s = sum(weights)
        left, right = min_s, max_s + 1# 搜索范围：[left, right)
        while left < right: # left == right时，搜索范围内无值，跳出循环
            mid = left + (right - left) // 2
            if can_finish(mid, weights, D):
                right = mid # 收缩右侧边界到符合要求的点（有效点）
            else:
                left = mid + 1  # 不断右移，寻找左边界点
        return left



