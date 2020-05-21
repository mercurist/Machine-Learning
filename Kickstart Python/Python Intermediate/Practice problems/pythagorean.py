t = int(input())


for t in range(t):

    n = int(input())
    for i in range(n + 1):
        for j in range(i + 1, n + 1, 1):
            if i**2 + j**2 == n:
                print("(" + str(i) + "," + str(j) + ")", end=" ")
