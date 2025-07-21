from inheritance import Animal, Dog

dog1 = Dog("방울이")
#isinstance(객체, 클래스): 객체가 해당 클래스 또는 부모 클래스의 인스턴스인지 확인
print(isinstance(dog1, Dog))
print(isinstance(dog1, Animal))

animal1 = Animal("일반 동물")
print(isinstance(animal1, Dog))
print(isinstance(animal1, Animal))

#person 클래스, student 클래스, teacher 클래스
#student랑 teacher person 상속
#person 속성으로 name
#student 속성으로 grade
#teacher 속성으로 subject

#일반 함수 정의
#매개변수로 클래스의 객체를 넣으면 if문으로 student클래스의 객체이면
#**학년 학생입니다. 출력
#teacher클래스면 **과목 선생님입니다. 출력
#person이면 일반 시민입니다. 출력

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

def process_person(obj):
    if isinstance(obj, Student):
        print(f"{obj.grade}학년 {obj.name}학생입니다.")
    elif isinstance(obj, Teacher):
        print(f"{obj.subject}담당 {obj.name}선생님입니다.")
    elif isinstance(obj, Person):
        print(f"일반 시민 {obj.name}입니다.")
    else:
        print("알 수 없는 타입의 객체입니다.")

person1 = Person("곽민성")
student1 = Student("최유지", 2)
teacher1 = Teacher("이동윤", "파이썬")

process_person(person1)
process_person(student1)
process_person(teacher1)
str1 = "abc"
process_person(str1)





