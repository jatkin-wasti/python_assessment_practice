# Declare a list with numbers 1 to 5 and add 6 at the end of the list
# num_list = [1, 2, 3, 4, 5]
# print(num_list)
# # appending 6 to the end of the list
# num_list.append(6)
# print(num_list)

# Create a tuple with numbers 1 to 5 and add 2.5
# num_tuple = (1, 2, 3, 4, 5)
# print(num_tuple)
# tuples are immutable so we can't add to it without converting it to a list and back again
# my_list = list(num_tuple)
# my_list.append(2.5)
# num_tuple = tuple(my_list)
# print(num_tuple)

# Creating a dictionary and changing a value
# num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# print(num_dict)
# num_dict["four"] = "four"
# print(num_dict)

# Create a set and output values from it until you output 3
# rand_set = {1, 2, 3, 4, 5}
# for num in rand_set:
#     print(num)
#     if num == 3:
#         break

# Declare dictionary of a shopping list with 3 items and print out a price for one of the items
# shopping_list = {"Milk": 0.85, "Bread": 0.80, "Crisps": 1.00}
# print(type(shopping_list))
# print(shopping_list["Bread"])

# Replace the price for Bread with 1.45
# shopping_list["Bread"] = 1.45
# print(shopping_list["Bread"])

# Declare a function that takes one argument
# def add(val1, val2):
#     return val1 + val2
#
#
# print(add(6, 7))

# Create Person class with name and age
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# test = Person("Jeff", 56)  # Instantiating an object of the class
# print(f"Hello {test.name}, you are {test.age} years old")

# Create a Student class that inherits from the Person class
# class Student(Person):
#     def __init__(self, name, age, student_id, course):
          # Super is used if you want to use or have access to class attributes or methods from a parent class
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.course = course
#
#
# student_test = Student("Jeff", 14, 212051, "DevOps")
# print(f"Hello {student_test.name}, you are {student_test.age} years old.\n"
#       f"Your student id is {student_test.student_id}, and you are enrolled in the {student_test.course} course")

# Create a dictionary with four shopping items and print out the total cost of the shopping list
# Iteration 1
# shopping_list = {"Milk": 0.85, "Bread": 0.80, "Crisps": 1.00, "Chocolate": 0.95}
# print(shopping_list)
# price = 0
# for keys in shopping_list:
#     price += shopping_list[keys]
# print(price)
# # a non looping way of doing the same task
# alternative_price = sum(shopping_list.values())
# print(alternative_price)
# Iteration 2
# def calc_price(dictionary):
#     price = 0
#     for keys in dictionary:
#         price += dictionary[keys]
#     print(price)
#
#
# shopping_list = {"Milk": 0.85, "Bread": 0.80, "Crisps": 1.00, "Chocolate": 0.95}
# calc_price(shopping_list)

# Add an item to the shopping list dictionary between bread and crisps
shopping_list = {"Milk": 0.85, "Bread": 0.80, "Crisps": 1.00, "Chocolate": 0.95}
# Dictionaries are indexed by the key not the index itself so  we can't  do this without splitting the dict,
# adding it, then rejoining the lists
# shopping_list["Kiwis"] = 3
# print(shopping_list)

# Create a list with the same values as our shopping list
shopping_list = ["Milk", "Bread", "Crisps", "Chocolate"]
print(shopping_list)
for items in shopping_list:
    if items == "Crisps":
        break
    print(items)
