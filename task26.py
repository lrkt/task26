class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self._breed = breed
        self.__age = age

    def animal_info(self):
        return f"Тварина на ім'я {self.name}, порода - {self._breed}, {self.get_age()}."
    
    def get_age(self):
        return self.__age


class Cat(Animal):
    def __init__(self, name, breed, age, sex):
        super().__init__(name, breed, age)
        self.sex = sex

    def animal_info(self):
        if self.sex == "Самець":
            return f"Кіт на ім'я {self.name}, порода - {self._breed}, {self.get_age()}."
        elif self.sex == "Самка": 
            return f"Кішка на ім'я {self.name}, порода - {self._breed}, {self.get_age()}."
        else:
            return f"Кіт(кішка) на ім'я {self.name}, порода - {self._breed}, {self.get_age()}."
        
    def noise(self):
        return "Meow, meow"
        

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def animal_info(self):
        return f"Собака на ім'я {self.name}, порода - {self._breed}, {self.get_age()}."
    
    def noise(self):
        return "Woof, woof"


cat = Cat("Гризлик", "Мейн-кун", 1, "Самець")
print(cat.animal_info())
print(cat.noise())

dog = Dog("Бен", "Ротвейлер", 5)
print(dog.animal_info())
print(dog.noise())