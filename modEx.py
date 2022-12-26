def add(a, b):

    c = a + b
    print("Addition of 2 values", c, __name__)


def sub(a, b):
    c = a - b
    print("Subtraction ", c)


def div(a, b):
    c = a / b
    print(c)


def mul(a, b):
    c = a * b
    print(c)


def main():
    print("from main function")
    add(3, 4)
    sub(5, 3)


if __name__ == "__main__":
    main()


