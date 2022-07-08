num = 0


while True:
    try:
        print("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
        num = int(input())

    except ValueError:
        print("정수를 입력하세요. ")

    else:
        while True:
            if num in range(1, 4):
                break

            else:
                try:
                    print("1,2,3 중 하나를 입력하세요.")
                    num = int(input())
                except ValueError:
                    print("정수를 입력하세요. ")
        break
    break

a = list()
for i in range(1, num+1):
    print('playerA : ', i)
    a.append(i)


while True:

    while True:
        try:
            print("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
            num = int(input())

        except ValueError:
            print("정수를 입력하세요. ")

        else:
            while True:
                if num in range(1, 4):
                    break

                else:
                    try:
                        print("1,2,3 중 하나를 입력하세요.")
                        num = int(input())
                    except ValueError:
                        print("정수를 입력하세요. ")
            break
        break

    for i in range(len(a)+1, len(a)+num+1):
        print('playerB : ', i)
        a.append(i)
        if i == 31:
            break

    while True:
        try:
            print("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
            num = int(input())

        except ValueError:
            print("정수를 입력하세요. ")

        else:
            while True:
                if num in range(1, 4):
                    break

                else:
                    try:
                        print("1,2,3 중 하나를 입력하세요.")
                        num = int(input())
                    except ValueError:
                        print("정수를 입력하세요. ")
            break
        break

    for i in range(len(a)+1, len(a)+num+1):
        print('playerA : ', i)
        a.append(i)
        if i == 31:
            break

    if i == 31:
        break
