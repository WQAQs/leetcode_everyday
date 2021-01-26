# 337. 打家劫舍 III
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

# 示例 1:

# 输入: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \ 
#      3   1

# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 示例 2:

# 输入: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1

# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        node_dict = {}

        # 方法1. 使用备忘录 + 动态规划 + 递归
        def dp(root):
            nonlocal node_dict
            if root == None: return 0
            if root in node_dict:
                return node_dict[root]
            left = root.left
            right = root.right
            rob_left, rob_right = 0, 0
            if left != None:
                rob_left = dp(left.left) + dp(left.right)
            if right != None:
                rob_right = dp(right.left) + dp(right.right)
            rob = root.val + rob_left + rob_right
            not_rob = dp(left) + dp(right)
            node_dict[root] = max(rob, not_rob)
            return node_dict[root]

        return dp(root)

        # 方法2. 不使用备忘录，状态压缩
        # 因为只用到了子节点抢或不抢
        def dp(root):
            if root == None: return [0, 0] # 注意这里不要写成 return 0
            left_arr = dp(root.left)
            right_arr = dp(root.right)
            rob = root.val + left_arr[0] + right_arr[0]
            not_rob = max(left_arr[0], left_arr[1]) + max(right_arr[0], right_arr[1])
            return [not_rob, rob]
        
        res_arr = dp(root)
        return max(res_arr[0], res_arr[1])
