#부모 클래스(Super Class)


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 동물 개체 생성!")

    def speak(self):
        print("동물이 소리를 냅니다.")

    def move(self):
        print(f"{self.name}이(가) 움직입니다.")

#====================상속 시작==================

#자식 클래스 (Sub Class)
#괄호 안에 부모 클래스 이름을 명시해서 상속 선언
class Dog(Animal):
    def wag(self):
        print(f"{self.name}이(가) 꼬리를 흔듭니다.")

    def speak(self): #부모 클래스의 speak 메소드를 재정의(Overriding)
        print("왈왈")


class Cat(Animal):
    def speak(self):
        print("애옹")

    def climb(self):
        print(f"{self.name}이(가) 높은곳에 올라갑니다.")


animal1 = Animal("일반 동물")
animal1.move()
animal1.speak()

dog1 = Dog("방울이")
dog1.speak()
dog1.move()
dog1.wag()

cat1 = Cat("냐옹이")
cat1.speak()
cat1.move()
cat1.climb()



#실습문제
#Shape 라는 부모 클래스 => 속성 : color
#메소드 describe =>이 도형의 색깔은 ***입니다. 출력

#Circle 자식 클래스
#메소드 describe 오버라이딩 => 이 원의 색깔은 ***입니다. 출력
#메소드 get_area(rafius) => >math.p1 모듈을 이용해서 넓이 구해서 리턴 print할때(소수점 둘째자리까지)

import math

class Shape:
    def __init__(self, color):
        self.color = color

    def descibe(self):
        print(f"이 도형의 색깔은 {self.color} 입니다.")


class Circle(Shape):
    def describe(self):
        print(f"이 원의 색깔은 {self.color} 입니다.")

    def get_area(self, rafius):
        return math.pi * (rafius ** 2)

circle1 = Circle("빨간색")
circle1.descibe()
print(f"원의 넓이 :{circle1.get_area(5) : .2f}") #소수점 둘째자리까지 표시 f-string








