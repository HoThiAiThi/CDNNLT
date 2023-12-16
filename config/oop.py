# class Employee:
# # Khai báo properties và gán giá tr ị cho chúng
#     def __init__(self, ID = None, salary = 0, department = None):
#         self.ID = ID
#         self.salary = salary
#         self.department = department
# # Tạo một object của class Employee v ới các tham s ố mặc định
# steve = Employee()
# # Tạo một object của class Employee v ới tham số của chúng ta
# mark = Employee( "3789", 2500, "Human Resources" )
# # In ra properties c ủa mark và steve
# print("steve")
# print("ID :", steve.ID)
# print("Salary :", steve.salary)
# print("Department :" , steve.department)
# print("mark")
# print("ID :", mark.ID)
# print("Salary :", mark.salary)
# print("Department :" , mark.department)
# class Player:
#     team_name = 'Manchester City' # class variable
#     def __init__(self, name):
#         self.name = name # instance variable
# Marland = Player('Marland')
# print(Marland.team_name + ',' + Marland.name)
# class MyClass():
#     def __init__(self):
#         self.__superprivate = "Hello"
#         self._semiprivate = ", world!"
# mc = MyClass()
# print(mc._semiprivate)
# # print(mc.__superprivate)
# class Employee:
#     def __init__(self, ID, salary):
#         self.ID = ID
#         self.__salary = salary # salary là một private property
#     def display_salary(self): # display_salary là một public method
#         print("Salary:", self.__salary)
#     def __display_id(self): # display_id là một private method
#         print("ID:", self.ID)

# steve = Employee(3789, 2500)
# steve.display_salary()
# steve.__display_id() # dòng này sẽ gây lỗi


# class Vehicle:
#     def __init__(self, make, color, model):
#         self.make = make
#         self.color = color
#         self.model = model
#     def print_details (self):
#         print("Manufacturer:" , self.make)
#         print("Color:", self.color)
#         print("Model:", self.model)
# class Car(Vehicle):
#     def __init__(self, make, color, model, doors):
# # gọi constructor (initializer) t ừ parent class
#         Vehicle.__init__(self, make, color, model)
#         self.doors = doors
#     def print_car_details (self):
#         self.print_details()
#         print("Doors:", self.doors)
# obj1 = Car( "Suzuki", "Grey", "2015", 4)
# obj1.print_car_details()

class Retangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return (self.length * self.width)
    def get_primeter(self):
        return 2* (self.length + self.width)

my_retangle = Retangle(5,3)
area = my_retangle.get_area()
primeter =my_retangle.get_primeter()
print(area)
print(primeter)



