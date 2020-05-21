n = int(input())

i = 2
flag = True
while i**2 <= n:
    if (n % i == 0):
        flag = False
        break
    i += 1

if flag:
    print("Prime")
else:
    print("Not Prime")
