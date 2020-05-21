def pattern(x):
    for i in range(x, 0, -1):
        j = 1
        quantity = x - i
        while (j <= i):
            print(j, end=" ")
            j += 1
        for k in range(2*quantity - 1):
            print("*", end=" ")
        print()


def main():
    x = int(input())
    pattern(x)


if __name__ == '__main__':
    main()
