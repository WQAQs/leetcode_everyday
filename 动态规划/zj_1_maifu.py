# dp
def find_preDj(nums, j, D):
    i = j
    while i > 0 and nums[j] - nums[i] <= D:
        i -= 1
    return i

N, D = map(int, input().split())
nums = list(map(int, input().split()))
m = len(nums) # 建筑总个数
# 1. 定义dp[i][j]为前i个人埋伏在前j栋建筑(并且最大距离不超过D），的埋伏方案总数（这里是全排列，最后再去重）
# i~[0,3] , j~[0,m]
dp = [[0]*(m + 1) for i in range(3 + 1)] # 初始化
# 2. 设置边界值
for j in range(1, m + 1):
    dp[1][j] = j
# 3. 遍历赋值dp数组——状态转移
for i in range(2, 3 + 1): # （1）【i个人的状态】遍历：i ~ [1, 3] 
    for j in range(1, m + 1):  # （2）【j栋建筑的状态】遍历：j ~ [1, m + 1] 
        # 可以做栋不同选择：
        #    （1）埋伏在nums[j]位置：
        #        则前i-1个人可以埋伏的范围在第多少栋之间：[preDj,j-1]，
        #        这个范围内的方案总数为：dp[i - 1][j-1] - dp[i - 1][preDj]
        #    （2）不埋伏在nums[j]位置:
        #         dp[i][j - 1]
        preDj = find_preDj(nums, j - 1, D) # 从第j栋建筑往前数，第1个到第j栋建筑距离超过D的建筑
        dp[i][j] = (dp[i - 1][j-1] - dp[i - 1][preDj]) + dp[i][j - 1]

res = dp[3][m] // 3*2*1 # 去重得到组合数
print(res)

# 5 19
# 1 10 20 30 50

# 4 3
# 1 2 3 4