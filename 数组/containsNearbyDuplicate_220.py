class Solution:
    # 方法1: 使用python字典，不超时
    # 字典支持在常量时间内完成 搜索，删除，插入
<<<<<<< HEAD
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict()
        for i, num in enumerate(nums):
            if num in dic and (i - dic[num]) <= k :
                return True
            else:
                dic[num] = i
        return False

class Solution:
    # 思路：使用python字典，不超时
    # 字典支持在常量时间内完成 搜索，删除，插入
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        dic = dict()
        for i, num in enumerate(nums):
            if num in dic and (i - dic[num]) <= k:
                return True
            else:
                dic[num] = i
        return False
=======
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        all_bucket = {} # 使用字典，避免超时
        bucket_size = t + 1 #保证在一个桶内的大小最大相差为t
        for i, num in enumerate(nums):
            index = num // bucket_size #计算桶索引（这里的索引即为字典的key）
            if index in all_bucket: #num所在桶已经存在（已经放进去了元素），返回True
                return True
            all_bucket[index] = num #放入桶中
            ##检查相邻桶中是否有满足条件的元素
            if index - 1 in all_bucket and abs(all_bucket[index - 1] - num) <= t:
                return True
            if index + 1 in all_bucket and abs(all_bucket[index + 1] - num) <= t:
                return True 
            if i >= k:
                all_bucket.pop(nums[i - k] // bucket_size) #保证所有桶中的索引最多比i小k
        return False


>>>>>>> db48d1d0a73b96d2dd1ead6aa1a3f9d7856347b1
