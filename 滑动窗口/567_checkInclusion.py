# 567. 字符串的排列
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

# 换句话说，第一个字符串的排列之一是第二个字符串的子串。

# 示例1:

# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
 

# 示例2:

# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
 

# 注意：

# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间


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

# 解题思路：使用滑动窗口
# 其实就是438题寻找异位字母

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0 # 使用滑动窗口 [left, right]
        window, needs = {}, {}
        match = 0 
        for c in s1:
            needs[c] = needs.get(c, 0) + 1
        while right <= len(s2) - 1:
            c = s2[right]
            if c in needs:
                window[c] = window.get(c, 0) + 1
                if window[c] == needs[c]:
                    match += 1
            while match == len(needs):
                if right - left + 1 == len(s1):
                    return True
                c = s2[left]
                if c in needs:
                    window[c] = window.get(c, 0) - 1
                    if window[c] < needs[c]:
                        match -= 1
                left += 1
            right += 1
        return False