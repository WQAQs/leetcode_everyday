class Solution:
    # 方法1: 
    # 只用了动态规划，k=4,n=5000就超时了
    def superEggDrop(self, K: int, N: int) -> int:
        # 理解“至少”：在最坏的情况下，最少需要抛的鸡蛋次数
        # dp[k][n]定义为鸡蛋个数为k，楼层总数为n，至少需要抛鸡蛋的次数
        dp = [[0] * (N + 1) for i in range(K + 1)]

        # dp数组初始化：
        for i in range(K + 1):
            dp[i][0] = 0 # 楼层总数为0时，抛鸡蛋次数为0
            dp[i][1] = 1 # 楼层总数为1时，抛鸡蛋次数为1
        for i in range(N + 1):
            dp[0][i] = 0 # 鸡蛋数为0时，怎么样子都检测不出来F的值，为了保证在状态转移的过程中，值被正确参考就可以。
            dp[1][i] = i # 鸡蛋数为1时，抛鸡蛋次数为楼层数n
        for k in range(2, K + 1): # 其他项最大初始化
            for n in range(2, N + 1):
                dp[k][n] = n

        for k in range(2, K + 1): # 归纳递推求dp数组
            for n in range(2, N + 1):
                for i in range(n): # 选择从哪个楼层抛下去
                    # 有两种情况：(1)鸡蛋碎了：dp[k - 1][i]
                    #           (2)鸡蛋没碎：dp[k][n - (i + 1)]
                    # max()取最坏的情况，min()取最好的楼层选择
                    dp[k][n] = min(dp[k][n], max(dp[k - 1][i], dp[k][n - (i + 1)]) + 1)  
        return dp[K][N]
                