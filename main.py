class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__phone = 'тринолятруляля'


    def get_age(self):
        return self.__age

    def set_age(self, age):
        if str(age).isdigit():
            if age > 0:
                self.__age = age

    def fun(self):
        print(self.name)

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.__age}'


obj = Student('Petro', 20)
obj.set_age(-56)
print(obj)
print(obj.get_age())

