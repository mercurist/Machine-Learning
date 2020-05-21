def generate(num, s):
    open_brac = 0
    close_brac = 0
    generate_helper(num, open_brac, close_brac, s)


def generate_helper(num, open_brac, close_brac, s):
    # print("checking for", end=" ")
    # print("".join(s))
    if (open_brac > num) or close_brac > open_brac:
        return

    if (open_brac == num) and (close_brac == num):
        print("".join(s))
        return

    s.append(")")
    generate_helper(num, open_brac, close_brac + 1, s)
    s.pop()

    s.append("(")
    generate_helper(num, open_brac + 1, close_brac, s)
    s.pop()

    pass


def main():
    num = int(input())
    s = []
    generate(num, s)


if __name__ == '__main__':
    main()
