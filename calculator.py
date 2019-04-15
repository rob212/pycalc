import sys


def calculate(a, b):
    sum= int(a) + int(b)
    return "sum is %d" % sum


if __name__=="__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    result = calculate(a, b)
    print(result)


