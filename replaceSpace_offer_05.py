class Solution:
    # 在 Python 和 Java 等语言中，字符串都被设计成「不可变」的类型，
    # 即无法直接修改字符串的某一位字符，需要新建一个字符串实现。
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == " ":
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)