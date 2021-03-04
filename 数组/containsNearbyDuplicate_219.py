class Solution:
    # 方法1: 使用python字典，不超时
    # 字典支持在常量时间内完成 搜索，删除，插入
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict()
        for i, num in enumerate(nums):
            if num in dic and (i - dic[num]) <= k :
                return True
            else:
                dic[num] = i
        return False
    
    # 方法2：使用队列，超时
    # 队列不支持在常量时间内完成 搜索，删除，插入
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        queue = deque()
        for num in nums:
            if num in queue:
                return True
            else:
                queue.append(num)
                if len(queue) > k:
                    queue.popleft()
        return False

