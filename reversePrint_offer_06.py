# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 方法1: 递归
    def reversePrint(self, head: ListNode) -> List[int]:
        return (self.reversePrint(head.next) + [head.val]) if head else []



class Solution:
    # 方法2: 翻转list模拟栈实现
    def reversePrint(self, head: ListNode) -> List[int]:
        mlist = []
        while head:
            mlist.append(head.val)
            head = head.next
        return mlist[::-1]