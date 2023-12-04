# 모듈
def add(a, b):
    return a+b
def minus(a, b):
    return a-b;
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

x = int(input("정수 입력: "))
y = int(input("정수 입력: "))

if __name__ == "__main__":
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {minus(x, y)}")
    print(f"{x} * {y} = {mul(x, y)}")
    print(f"{x} / {y} = {div(x, y)}")
