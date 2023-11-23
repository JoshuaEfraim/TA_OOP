class Person:
    def __init__(self, name, age):
        self._name = name  
        self._age = age    

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Invalid name format")

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 150:
            self._age = new_age
        else:
            print("Invalid age")

person = Person("John", 30)

print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Jane")
person.set_age(25)

# Displaying updated information
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())