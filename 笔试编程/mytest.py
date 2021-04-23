import sys
# 3 4
# 123
# sys.maxsize
# N, D = map(int, input().split()) # 
# nums = list(map(int, input().split()))
# print(nums)
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
#     2
# ) !
# ! @
    for i in range(n):
        nums = []
        line = sys.stdin.readline().strip()
        nums1_s, nums2_s = line.split()
        flag_1,flag_2 = 0,0 # 负数标志 
        # chs.append(values[:])
        # print(nums)
        mdict1 = {')': 0, '!':1, '@':2,'#':3,'$':4,'%':5,'^':6,'&':7,'*':8,')':9}
        mdict2 = {'-':'-','0':')','1': '!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':')'}
        # for c in range(len(chs)):
            # nums1_s = chs[0]
            # nums2_s = chs[1]
        # num = str(mdict.get(c))
        if nums1_s[0] == '-':
            nums1_s = nums1_s[1:]
            flag_1 = 1
        if nums2_s[0] == '-':
            nums2_s = nums2_s[1:]
            flag_2 = 1
        # nums.append(num)
        # 牛星文转数字
        def mfun1(s):
            res = 0
            for c in s:
                a = mdict1.get(c)
                res = res*10 + a
            return res
        # num1 = int(''.join(nums1_s))
        # num2 = int(''.join(nums2_s))
        num1, num2 = mfun1(nums1_s),mfun1(nums2_s)
        num1 = num1 if flag_1 == 0 else -1*num1
        num2 = num2 if flag_2 == 0 else -1*num2
        ans = num1 + num2
        sub1 = num1 + (-1)*num2
        sub2 = (-1)*num1 + num2
        # 数字转牛星文
        def mfun2(num):
            s = str(num)
            res = []
            for a in s:
                c = mdict2.get(a)
                res.append(c)
            return ''.join(res)
        # result = []
        # result.append(mfun2(ans))
        # result.append(mfun2(sub1))
        # result.append(mfun2(sub2))
        print(mfun2(ans))
        print(mfun2(sub1))
        print(mfun2(sub2))
        # print(result)
                
            
    