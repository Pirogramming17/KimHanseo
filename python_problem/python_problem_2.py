# 함수 이름은 변경 가능합니다.

# menu 1
from posixpath import split
from re import A

all_studentInfo = []


def Menu1(all_studentInfo, studentInfo):

    all_studentInfo[studentInfo[0]] = (
        int(studentInfo[1]), int(studentInfo[2]))
    # 사전에 학생 정보 저장하는 코딩

# menu 2


def Menu2(all_studentInfo):
    if len(all_studentInfo) != 4:
        if (score1+score2)/2 >= 90:
            all_studentInfo[studentInfo[0]].append('A')
        elif (score1+score2)/2 >= 80:
            all_studentInfo[studentInfo[0]].append('B')
        elif (score1+score2)/2 >= 70:
            all_studentInfo[studentInfo[0]].append('C')
        else:
            all_studentInfo[studentInfo[0]].append('D')
    # 학점 부여 하는 코딩

# menu 3


def Menu3(all_studentInfo):
    Menu1(name, score1, score2)
    print("-------------------------------")
    print("name mid final grade")
    print("-------------------------------")
    print(all_studentInfo)
    # 출력 코딩

# menu 4


def Menu4(studentInfo, all_studentInfo):
    if studentInfo['name'] == name:
        del all_studentInfo[name]

    # 학생 정보 삭제하는 코딩


# 학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            print("Enter name mid-score final-score")
            name = input()
            score1, score2 = map(int, input().split())
            studentInfo = list(name, score1, score2)
            if len(studentInfo) != 3:
                print("Num of data is not 3!")
            elif studentInfo[0] in all_studentInfo:
                print("Already exist name!")
            else:
                Menu1(all_studentInfo, studentInfo)
        except ValueError:
            print("Score is not positive integer!")

        # 학생 정보 입력받기
        # 예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        # 예외사항이 아닌 입력인 경우 1번 함수 호출

    elif choice == "2":
        if len(all_studentInfo) == 0:
            print("No student data!")
        else:
            Menu2(all_studentInfo)
            print("Grading to all students.")
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력

    elif choice == "3":
        if len(all_studentInfo) == 0:
            print("No student data!")
        elif len(studentInfo) != 4:
            print("There is a student who didn't get grade.")
        else:
            Menu3(all_studentInfo)
        # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        # 예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4":
        print("Enter the name to")
        name = input()
        if name in studentInfo:
            Menu4(studentInfo, all_studentInfo)
            print(name, "student information is deleted.")
        else:
            print("Not exist name!")

        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5":
        print("Exit Program!")
        break
        # 프로그램 종료 메세지 출력
        # 반복문 종료

    else:
        print("Wrong number. Choose again.")
        # "Wrong number. Choose again." 출력
