# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 示例 4:

# 输入: s = ""
# 输出: 0

# 提示：
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成



# 滑动窗口技巧
#
# 思路： right 先向右滑动，left再跟随滑动
#
# 模板：
#
# left, right = 0, 0
# while right < len(s):
#     res.append(s[right])
#     right += 1
#    
#     while valid:
#         res.pop(s[left])
#         left += 1
#   

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = {}
        res = 0
        while right < len(s):
            c1 = s[right]
            while c1 in window and window[c1] >= 1:
                c2 = s[left]
                window[c2] = window.get(c2, 0) - 1
                left += 1
            window[c1] = window.get(c1, 0) + 1
            res = max(res, right - left + 1)
            right += 1
        return res