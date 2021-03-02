# 438. 找到字符串中所有字母异位词
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

# 说明：

# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 示例 1:

# 输入:
# s: "cbaebabacd" p: "abc"

# 输出:
# [0, 6]

# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  示例 2:

# 输入:
# s: "abab" p: "ab"

# 输出:
# [0, 1, 2]

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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window, needs = {}, {}
        match = 0
        for c in p:
            needs[c] = needs.get(c, 0) + 1
        left , right = 0, 0
        while right < len(s):
            c = s[right]
            if c in needs:
                window[c] = window.get(c, 0) + 1
                if window[c] == needs[c]:
                    match += 1                   
            while match == len(needs):
                if right - left + 1 == len(p):
                    res.append(left)
                c = s[left]
                if c in needs:
                    window[c] = window.get(c, 0) - 1
                    if window[c] < needs[c]:
                        match -= 1
                left += 1
            right += 1
        return res