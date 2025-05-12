class First :
    name = "first"
    def __init__(self) :
        print("First class")
    
    def printFirst(self) :
        print("first")
        
class Second :
    name = "second"
    def __init__(self) :
        print("First class")
    
    @classmethod
    def printName(cls) :
        print(cls.name)

#상속해야 할 부모클래스가 두 개인 경우 충돌 가능
#파이썬은 MRO에 따라 다중 상속을 진행
class Third(First, Second) :
    pass

third = Third()
third.printName()
third.printFirst()