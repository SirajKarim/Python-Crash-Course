# class Dog():
#     def  __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def sit(self):
#         print(self.name.title() + " is now sitting")

#     def roll_over(self):
#         print(self.name.title() + " is now rolled over ")


# my_dog = Dog("tommy",14)
# print("My dog name is " +my_dog.name.title())
# print("My dog's age  is " + str(my_dog.age))
# my_dog.sit()
# my_dog.roll_over()


# my_dog = Dog("Sheru",17)
# print("My dog name is " +my_dog.name.title())
# print("My dog's age  is " + str(my_dog.age))
# my_dog.sit()
# my_dog.roll_over()

# # 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# # Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# # Make a method called describe_restaurant() that prints these two pieces of
# # information, and a method called open_restaurant() that prints a message indicating 
# # that the restaurant is open.
# # Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# class Restaurant():

#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print('Restaurant is open')
        
# my_restaurant = Restaurant('abc','xyz')
# print("Restaurant name is "+my_restaurant.restaurant_name.title()+" and cuisin type is "+my_restaurant.cuisine_type)
# my_restaurant.describe_restaurant()
# # 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# # different instances from the class, and call describe_restaurant() for each
# # instance.
# y_restaurant = Restaurant('aaa','bbb')
# y_restaurant.describe_restaurant()
# m_restaurant = Restaurant('ccc','ddd')
# m_restaurant.describe_restaurant()
# t_restaurant = Restaurant('eee','fff')
# t_restaurant.describe_restaurant()
# # Inheritence

class Car():
 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.batterysize = 60

    def descriptivebattery(self):
        print("The car has a battery of "+str(self.batterysize)+ "-kWh battery.")

my_tesla = ElectricCar('tesla','model x',2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.descriptivebattery())