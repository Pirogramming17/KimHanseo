num = 0

print('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
num = input()

while num != (1 or 2 or 3):
    if (str(type(num)) != "<class 'int'>"):
        print('정수를 입력하세요 >>')
        num = int(input())
    else:
        print('1, 2, 3 중 하나를 입력하세요 >>')
        num = int(input())

int(num)
