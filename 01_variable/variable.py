# 주석 처리 (컨트롤 + /)

# 변수
# 어떤한 값들을 상자에 담아 이름을 붙이는 것

#변수에 문자열 넣기
last_name  = "김"
#print("제 성은 " + last_name + " 입니다")
first_name = "영환"
name = last_name + first_name #문자열과 문자열은 더할 수 있다.
#print(name)
# a = name - last_name #문자열에서 뺄셈은 할 수 없다.

b = name * 3 #문자열을 곱해서 여러번 곱할 수 있다. 곱하기는 가능, 단 나누기는 할 수 없다.
#print(b)
#변수에 정수 넣기
age = 27
#print(age)
#변수에 실수 넣기
pie = 3.141592
#print(pie)
#변수에 여러줄을 문자열로 쓸 떄
str1 = """
안녕하세요
반갑습니다.
"""
#print(str1)
st2 = '''
안녕하세요.
반갑습니다.
'''
#print(st2)

num1 = 10
num2 = 20
#print(num1 + num2)
"""
컴퓨터는 이진수만 저장을 하게 되는데 소수는 정확하게 떨어지는 이진법으로 저장이 불가능하다. 그래서 근사값을 저장하고 연산을 하게 되면서 실제의
값보다 아주 조금 더 크게 나온다."""

#부동소수점의 오류
#4.2 + 2.1을 하면 6.3인데 6.3000000001이 나오는데 메모리 공간의 한계 때문에 이렇게 나온다.
#나머지는 버려지고 반올림해서 1로 끝난다. 그래서 메모리에 근삿값이 나온다.

#boolean
"""참과 거짓의 변수는 is 또는 has 또는 can 등을 앞에 붙여주는게 좋다.
부정은 보통 쓰지 않는다."""
is_mz = True

is_empty = False
str3 = "python" #이 변수 안에 문자열이 들어가 있지만 값이 있기 때문에 True이다.
str4 = "" #값이 없는 형태는 False.

#실습
#내 정보 출력해보기
name = "김영환"
height = 182.00
weight = 90.2
is_male = True

#print("내 이름은 " + name + " 입니다.")
#print("제 키는",height)
#print("제 몸무게는", weight)
#print("남자인가요?", is_male)

#변수로 출력해보기
#print(f"제 이름은 {name} 입니다., 제 몸무게는 {weight} \n 남자인가요? {is_male}") #안에서 중괄호에 변수를 넣을 수 있다.

#"안녕하세요" 출력하기
str5 = "\"안녕하세요\""
#print(str5)

num3 = 10
num4 = 20
print(f"num1 + num2 = {num3 + num4}")