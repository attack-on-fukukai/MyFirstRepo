def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def main():
    print(f"{1}と{2}を足すと{add(1, 2)}です。")
    print(f"{2}と{1}を引くと{sub(1, 2)}です。")


if __name__ == '__main__':
    main()
