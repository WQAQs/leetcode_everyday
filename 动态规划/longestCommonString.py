while True:
    try:
        s1 = input()
        s2 = input()
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        index, max_len = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        index = i
                else:
                    dp[i][j] = 0
        print(s1[index-max_len:index])
    except:
        break