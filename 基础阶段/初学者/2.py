# 输出九九乘法表
for x in range(1,10,1):
    for y in range(1,x+1,1):
        print(f"{y}x{x}={x*y}\t",end='')
    print()