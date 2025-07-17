#print(10/0)
from operator import index
from pydoc import classify_class_attrs

# try:
#     print(10/0) # 예외가 발생할 것같은 코드 (미리 예방)
# except:
#     print("예외 발생")

# try:
#     num = int(input("숫자를 입력하세요 :"))
#     print(10/num)
# except ValueError : # 값 데이터 오류
#     print("문자 말고 숫자 넣으셈")
# except ZeroDivisionError :
#     print("0말고 딴거 넣어라")

#IndexError, ValueError
# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스 : "))
#     print(my_list[index])
# except ValueError:
#     print("숫자만 입력해라")
# except IndexError:
#     print("그런 인덱스 없다")

#파일 입출력 예외 처리 : FileNotFoundError
# file = None
# try:
#     file = open("hi.txt", "r", encoding="utf-8")
#     content = file.read() # 파일의 내용을 읽어온다.
#     print(content)
# except FileNotFoundError:
#     print("그런 파일 없음")
# finally:
#     if file is not None and not file.closed:
#         file.close()
#         print("정상적으로 파일이 닫혔습니다.")
#     elif file is None:
#         print("애초에 열리지 않았음")

#리스트 요소 5개 선언하고 index로 찾는 로직
#Index, ValueError 예외 처리
#정상적이면 해당 리스트 값 출력
#마지막은 항상 끝!!출력하기

# my_list = [1, 2, 3, 4, 5]
# try:
#     index_input = input("인덱스를 입력")
#     index = int(index_input)
#     result = my_list[index]
# except IndexError as message: #원래 뜨던 메세지를 띄움
#     print("그런 인덱스 없다")
#     print(message)
# except ValueError as message:
#     print("숫자 입력해라")
#     print(message)
# else:
#     print(f"해당 인덱스의 값 : {result}")
# finally:
#     print("끝!!")

#raise 키워드 : 강제로 예외 발생시키기
#특정 조건에서 개발자가 직접 예외를 발생시키는데 사용
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise Exception("0이상 150미만 숫자만 입력해주세요.") #에러 메세지
# except Exception as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("끝!")

#사용자 정의 예외 클래스
# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0이상 150미만 숫자만 입력하세요")
#
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age <0 or age > 150:
#         raise AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("끝!")

#출금을 할때 잔액이 부족하면 발생되는 예외
#FoundError => 잔액이 부족합니다. 현재 잔액 ***원, 출금 시도 금액 ***원
#Account 클래스 만들고 메소드 withdraw 출금메소드
#출금을 할때 잔액이 부족하면 FundsError를 발생

class FundError(Exception):
    def __init__(self, balance, amount):#생성자에서 현재 잔액과 출금시도 금액 받기
        super().__init__(f"잔액이 부족합니다. 현재 잔액 {balance}원, 출금 시도 금액 {amount}원")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise FundError(self.balance, amount)
        except FundError as e:
            print(e)

        else:
            self.balance -= amount
            print(f"정상적으로 출금되었습니다. 남은 잔액 {self.balance}")

accont1 = BankAccount(100000)
accont1.withdraw(50000)
accont1.withdraw(80000)

#딕셔너리 요소 찾기
#딕셔너리 키를 입력 받음(숫자로)
#result 변수에 해당 키의 값을 넣음
#예외 처리 => 해당 키가 존재 하지 않을 때 "KeyError"처리 : "해당 키는 존재하지 않습니다."
#숫자가 아닌 문자를 입력했을때 : "ValueError"처리 : "숫자를 입력해 주세요."
#정상적으로 실행된다면 해당 키를 갑을 넣어둔 result 출력
#마지막은 항상 "완료"를 출력

key = input("키를 입력하세요 : ")
result = int(input(f"해당 키는 {key}입니다."))
try:



