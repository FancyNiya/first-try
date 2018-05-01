 def Move_Tower(n, a, b, c):
    count = 0
    if n==1:
        print(a, "==>", c)                # 将最后一个盘子移动到 c 上
        return 1                          # 移动一次                 
    else:
        count += Move_Tower(n-1, a, c, b) # 将 n-1 个盘子移动到 b 上，b 相当于一个缓冲区
        count += Move_Tower(1, a, b, c)   # 将 n-1 移动到 b 后, 将最后一个盘子直接放在 c 上
        count += Move_Tower(n-1, b, a, c) # 将 n-1 从缓冲区 b 移动到 c 上, 完成
        return count
