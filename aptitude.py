import numpy as np

for _ in range(int(input())):
    input()
    gpa = list(map(float, input().split()))
    maax = -2
    for i in range(5):
        xs = list(map(float, input().split()))
        cf = np.corrcoef(gpa, xs)[0,1]
        if cf > maax:
            maax = cf
            max_i = i
    print(max_i+1)