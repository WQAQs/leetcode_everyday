# import sys

if __name__ == "__main__":


# 1. 一行输入多个数
    # a,b =input('输入a,b空格隔开:').split()
    #此时a,b为str型
    t =map(int,input('输入a,b空格隔开:').split())
    a,b = t
    print(type(t))
    print(type(a))
    print(type(b))
    #此时a,b为int型

##  2. 输入一个整数告诉有多少行，再输入每组的具体值
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(type(a[0]))

## 3. 多组输入数据，但没指定多少组
    while True:
        try:
            strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
            a, b = map(int, input().strip().split())
            print(a+b)
        except EOFError: 
            break

# python 字符相减得到数字

# python中没有字符之间的直接相减运算，但可以通过ord()函数实现
# ord()函数主要用来返回对应字符的ascii码

# >>> ord('9')-ord('0')
# 9


# 输入输出流
# print list

# 数学运算
# 整除 //
# Python遵循的取整方式为：向下取整

# 取余 %
# 取余结果 = 被除数 - 除数 * 整除结果

# eg：  -10 % 3 = -10 - 3 * (-4) = 2

# 整除	取模(求余)
# 10 // 3 = 3	10 % 3 = 1
# 10 // -3 = -4	10 % -3 = -2
# -10 // 3 = -4	-10 % 3 = 2
# -10 // -3 = 3	-10 % -3 = -1
# 常用函数
# 求长度
# len(list)

# 求最大值/最小值：
# max(val1, val2, val3)

# 求和sum()
# 内置求和函数sum(iterable, start = 0)

# # Return the sum of a 'start' value (default: 0) plus an iterable of numbers
 
# max_s = sum(weights)
# 排序
# （1）原地排序 list.sort()
# （2）自定义排序：sorted(iterable[, cmp[, key[, reverse]]])
# 特点：可以对所有可迭代的对象进行排序操作。返回的是一个新的 list，不修改原来的对象。

# 参数：

# iterable – 可迭代对象。

# cmp – 可选，比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。

# key – 可选，主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。

# reverse – 可选，排序规则，reverse = True 降序 ，reverse = False 升序（默认）。

# 1. 按照第一个元素排序
# sorted(a, key=lambda x:x[0])

# >>> [('a',2),('b',3),('c',1),('d',4)]

# 2. 自定义比较函数
# functools.cmp_to_key()将cmp函数转化为 key。

# # 先比较第一个数的大小，再比较第二个数的大小
# def compare(a, b): 
#     if a[0] != b[0]:
#         return -1 if a[0] < b[0] else 1
#     else: 
#         if a[1] < b[1]:
#             return -1
#         elif a[1] > b[1]:
#             return 1
#     else: return 0
 
# s = [[1,6],[2,3],[1,4],[3,5]]
# s = sorted(s, key=functools.cmp_to_key(compare))
# print(s) # [[1, 4], [1, 6], [2, 3], [3, 5]]
 
# lambda表达式
# 定义：lambda表达式是一行的函数。它们在其他语言中也被称为匿名函数，即函数没有具体的名称，

# # 可直接调用/保存并调用：
 
# add = lambda x, y: x + y # 保存niming print(add(3, 5)) # 调用函数
# list
# 1. 初始化
# mlist = [6,0,3]

# 2. 访问/修改元素
# val = mlist[0] , mlist[0] = 1

# 3. 添加元素
# 末尾添加： mlist.append(val)
# 指定位置添加元素：list.insert（n,'4'）
# 若指定的下标不存在，那么就是在末尾添加

# 4. 删除元素
# mlist.pop() # 删除最后一个元素
 
# mlist.pop(n) # 删除指定下标的元素
 
# del mlist[0] # 删除指定下标的元素
# 5. 切片
# 返回副本：
# t = mylist[:]    要使用这个，不然可变对象的值会被覆盖！！！！！

# 倒序：
# t = mlist[::-1]

# 6.列表生成器
# # 一维列表 
# list = [x * x for x in range(1,11)]
 
# # 二维列表 
# list = [[0] * m for i in range(n)] # 生成n行m列的二维
# list list = [m + n for m in 'ABC' for n in 'XYZ'] # 两层循环，生成全排列
# 7.函数中返回一个新的list： return [val1, val2]
# 8. 计数count()
# 统计list中某元素次数
# aList = [123, 'xyz', 'zara', 'abc', 123]
 
# print "Count for 123 : "
 
# aList.count(123)
# 遍历list
# for i, num in enumerate(nums):
# 队列
# from collections import deque
 
# mq = deque() mq.append(val) #末尾添加元素
 
# mq.popleft() #队首取出元素
# 哈希表
# 1. 初始化：
# （1） mdict = dict()
 
# （2） mdict = {}
 
# 2. 添加/修改键值对：
# mdict[key] = val # mdict中没有key则添加键值对，有key则修改查出来的键对应对值为val
 
# # ！！！！！ 注意不能自增
# # 要取出来再加1
# # eg：
# mdict[key] = mdict.get(key,0) + 1
# 3. 根据key查询val：
#    dict.get(key, default=None)

# val = mdict.dict.get(key) # key 不存在返回None 
# val = mdict.dict.get(key, 0) # key 不存在返回0
# 最小堆heapq
# import heapq
 
# 1. 构建最小堆
# heap = [22, 4, 8, 1] # 定一个list
# heapq.heapify(list) # 原地将一个list转换为一个最小堆
 
# 2. 添加元素
# heapq.heappush(heap, num)  # 加入堆
 
 
# 3. 访问堆内容
 
# ## 弹出堆顶元素，即最小元素
# print(heapq.heappop(nums)) 
# # out: 2
 
 
# 4. 堆排序
 
# ## 获取所有堆排序后的元素
# result = [heapq.heappop(nums) for _ in range(len(nums))]
# print(result)
# # out: [1，8，4，22]
 
# ## 获取堆最大或最小值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数
 
# ## 限定排序范围，返回堆排序后的结果
# nums = [1, 3, 4, 5, 2]
# print(heapq.nlargest(3, nums)) # 返回nums最大的3个元素
# print(heapq.nsmallest(3, nums))  # 返回最大的3个元素
 
# """
# 输出：
# [5, 4, 3]
# [1, 2, 3]
# """
 
# ## 自定义堆排序key
 
# 这两个函数还接受一个key参数，用于dict或其他数据结构类型使用
 
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# pprint(cheap)
# pprint(expensive)
 
# """
# 输出：
# [{'name': 'YHOO', 'price': 16.35, 'shares': 45},
#  {'name': 'FB', 'price': 21.09, 'shares': 200},
#  {'name': 'HPQ', 'price': 31.75, 'shares': 35}]
# [{'name': 'AAPL', 'price': 543.22, 'shares': 50},
#  {'name': 'ACME', 'price': 115.65, 'shares': 75},
#  {'name': 'IBM', 'price': 91.1, 'shares': 100}]
# """
 
# 4. heapq应用
 
# 实现heap堆排序算法
 
# >>> def heapsort(iterable):
# ...     h = []
# ...     for value in iterable:
# ...         heappush(h, value)
# ...     return [heappop(h) for i in range(len(h))]
# ...
# >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 该算法和sorted(iterable) 类似，但是它是不稳定的。
 
# 堆的值可以是元组类型，可以实现对带权值的元素进行排序。
 
# >>> h = []
# >>> heappush(h, (5, 'write code'))
# >>> heappush(h, (7, 'release product'))
# >>> heappush(h, (1, 'write spec'))
# >>> heappush(h, (3, 'create tests'))
# >>> heappop(h)
# (1, 'write spec')
#  
    # for line in sys.stdin:
    #     a = line.split()
    #     print(int(a[0]) + int(a[1]))
    # 控制台输入
    # a = sys.stdin.readline().split()
    # print(int(a[0] + a[1]))

    # l = []
    # l.append('')
    # l.append('')
    # print(len(l)) # 输出2 ，空字符也是字符，占位子

#       raw_input()          #' insert 0 5     '
#       raw_input().strip()  #'insert 0 5'
#       raw_input().strip().split()  #['insert', '0', '5']


# import java.io.BufferedInputStream;
# import java.io.BufferedOutputStream;
# import java.io.PrintWriter;
# import java.util.Scanner;

# public class AL_2 {
#     public static Scanner in = new Scanner(new BufferedInputStream(System.in));
#     public static PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

#     public static void main(String[] args) {
#         while(true){
#             int n = sc.nextInt();
#             double sum = 0;//每种情况燃烧时间的和
#             long count = 0;//可能的分割情况个数
#             for(int  i = 1; i < n;i++){
#                 //第一次分割
#                 int  j = n-i;
#                 int max = Math.max(i, j);
#                 int min = Math.min(i,j);
#                 max -= min;//燃烧完短的，长的部分剩下的长度
#                 if(max >= 2){//进行第二次分割
#                     for(int m = 1; m < max; m++){
#                         sum += min;//加上短的那部分燃烧的时间
#                         count++;//情况个数加一
#                         int remain = max - m;
#                         sum += Math.max(m,remain);//第二次分割完，燃烧时间应该是长的那部分的燃烧时间
#                     }
#                 }else{
#                     count++;//没进行第二次分割：比如：3，2
#                     sum += Math.max(i, j);//燃烧时间直接加上长的那部分需要的燃烧时间
#                 }
#             }
#             System.out.printf("%.4f\n",sum/count);
#         }
#     }
# # }
import java.util.*;
class test{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        List list = new LinkedList();
        while(in.hasNext()){
            int k = in.nextInt();
            int[] arr = new int[k];
            for (int i = 0; i < k; i++){
                arr[i] = in.nextInt();
            }
            list.add(arr);
        }
        LinkedList cur = new LinkedList();
        helper(list, m, cur);
        int res = helper(cur, m, n);
        System.out.println(res);
    }
 
    private static int helper(List cur, int m, int n){
        int[][] dp = new int[n][m + 1];
        for (int i = 0; i < n; i++){
            for (int j = 0; j <= m; j++){
                if (i == 0 && j != 0) {
                    dp[i][j] = cur.get(0)[j-1];
                }else if (j == 0) {
                    dp[i][j] = 0;
                }else {
                    int curMax = dp[i-1][j];
                    for (int k = 0; k <= j; k++){
                        curMax = Math.max(curMax, dp[i-1][j-k] + cur.get(i)[k]);
                    }
                    dp[i][j] = curMax;
                }
            }
        }
        return dp[n-1][m];
 
    }
 
    private static void helper(List list, int m, List resList){
        for (int[] cur : list){
            resList.add(genRow(cur, m));
        }
    }
 
    private static int[] genRow(int[] arr, int m){
        int[] res = new int[m+1];
        res[0] = 0;
        for (int i = 1; i <= m; i++){
            res[i] = maxSum(arr, i);
        }
        return res;
    }
 
    private static int maxSum(int[] arr, int m){
        int sum = 0;
        for (int i : arr) sum += i;
        if (m > arr.length) return sum;
        int res = Integer.MAX_VALUE;
        for (int i = 0; i <= m; i++){
            int cur = 0;
            for (int j = 0; j < arr.length - m; j++){
                cur += arr[i+j];
            }
            res = Math.min(res, cur);
        }
        return sum - res;
    }
}

