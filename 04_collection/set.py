#세트
#중복이 없고 순서가 없음,중괄호
fruits = {"사과", "바나나", "오렌지", "바나나"}
print(fruits)
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)

empty_set = set() # 비어있는 세트

#요소 추가
s = {1, 2, 3,}
s.add(4) #요소 한개만 추가할때
print(s)

s.update([5, 6, 7]) #여러개를 한번에 추가할때
print(s)

#요소 삭제
s.remove(3) #존재하지 않는 값 제거 시 오류 발생
s.discard(10) #존재하지 않는 값 제거 시 오류 없음
print(s)

s.clear()
print(s)

A = {1, 2, 3, 4, 5}
B ={ 4, 5, 6, 7, 8}

print(A | B) # 합집합
print(A.union(B))

print(A & B) #교집합
print(A.intersection(B))

print(A - B) #차집합
print(A.difference(B))

#실습
python_class = {"철수", "영희", "민수", "지수"}
java_class = {"영희", "민수", "지훈", "길동"}

#파이썬과 자바 수업을 둘다 듣는 사람 출력
#파이썬만 듣는 사람 출력
#자바만 듣는 사람 출력

print(python_class.intersection(java_class))
print(python_class.difference(java_class))
print(java_class.difference(python_class))







