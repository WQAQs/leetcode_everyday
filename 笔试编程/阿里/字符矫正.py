n = int(input())
for j in range(n):
    ts = list(input())
    if len(ts) <= 1: print(ts)
    f1, f2 = 0, 0
    i = 0
    # while i < (len(ts) - 1):
    while i  < (len(ts) - 1):
        print(i)
        # （1）3个数连一起
        l = len(ts)
        while ts[i] == ts[i + 1] and i + 2 < len(ts) and ts[i] == ts[i + 2]:
            # 去掉i+2位置元素
            ts[: i+3] = ts[:i+2]
            
        # （2）2个数连一起 第一次
        if ts[i] == ts[i + 1]:
            f1 += 1
        # （3）2个数连一起 第二次
        if f1 == 2: # 去掉i+1位置元素
            ts[ : i+2] = ts[:(i + 1)]
            f1 = 0
        i += 1
    print(''.join(ts))