class Solution:
    # 方法1:哈希表
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

class Solution:
    # 方法2:原地交换
    # 思想：利用索引与数字一一对应的关系 
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i: 
                i += 1
                continue
            if nums[nums[i]] == nums[i]: #寻找到了重复的元素
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]] #把元素放在应该放的索引上（保持索引与数字一一对应的关系）

class Solution:
    # 方法3: 排序，线性搜索并比较
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return None