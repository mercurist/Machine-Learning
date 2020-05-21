def printSum(list):
    sum = 0
    for x in list:
        sum += x
    return sum


if __name__ == "__main__":
    # specify what to do when this module is run directly
    print("Executing directly")
    print("My module name = %s" % (__name__))
else:
    print("Imported from somewhere else")
