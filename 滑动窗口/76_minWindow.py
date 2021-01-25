# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
 
# 示例 1：

# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例 2：

# 输入：s = "a", t = "a"
# 输出："a"
 

# 提示：

# 1 <= s.length, t.length <= 105
# s 和 t 由英文字母组成


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
    def minWindow(self, s: str, t: str) -> str:
        left, right, start = 0, 0, 0
        needs, window, match = {}, {}, 0
        res_len = len(s) + 1
        for c in t:
            needs[c] = needs.get(c, 0) + 1
        while right < len(s): 
            c1 = s[right]
            if c1 in needs:
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            while match == len(needs):
                if right - left + 1 < res_len:
                    start = left
                    res_len = right - left + 1
                c2 = s[left]
                if c2 in needs:
                    window[c2] = window.get(c2, 0) - 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
            right += 1
        return s[start : start + res_len] if res_len != len(s) + 1 else ""