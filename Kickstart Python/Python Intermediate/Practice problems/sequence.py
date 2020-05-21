n = int(input())
prev = None
temp = None
flag = True
is_decreasing = True
is_increasing = False
for i in range(n):
    if temp is None:
        temp = int(input())
        prev = temp
        continue
    temp = int(input())
    if is_decreasing:
        if(temp < prev):
            continue
        if (temp == prev):
            flag = False
            break
        if (temp > prev):
            is_decreasing = False
            is_increasing = True
            continue

    if is_increasing:
        if (temp <= prev):
            flag = False
            break

if flag:
    print("true")
else:
    print("false")
