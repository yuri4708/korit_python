# 조건문
"""
if 조건 :
    실행할 코드
"""
from selectors import SelectSelector

# num = int(input("숫자를 입력하세요 : ")) #input 문자열이 정수로 변환(int ())
# if num > 0 :
#     print("양수 입니다.")
# else:
#     print("이 숫자는 0이거나 음수입니다.")

#if - elid-else문
# score = int(input("점수를 입력해주세요 : "))
#
# if score >= 90:
#     print("A 학점입니다.")
# elif score >= 80:
#     print("B 학점입니다.")
# elif score >= 70:
#     print("C 학점입니다.")
# elif score >= 60:
#     print("D 학점입니다.")
# else:
#     print("F 학점입니다.") #가장 먼저 참인 조건을 만나면 밑에 있는 코드는 적용 안됨

#실습
#숫자를 입력받고 조건문으로 홀짝 판별
#
# number = int(input("숫자를 입력하세요 : "))
# if number % 2 == 0 :
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

#나이를 입력받고 학생여부 입력받기(y/n)
#20세 이상이면서 학생이면 성인학생입니다.
#아니면 성인학생이 아닙니다.

age = int(input("나이를 입력하세요 :"))
student = input("학생인가요? - (y/n) :")
if age >= 20 and student == "y":
    print("성인학생입니다.")
else :
    print("성인학생이 아닙니다.")

