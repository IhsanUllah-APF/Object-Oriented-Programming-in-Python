# Bismillah

class Item:
    def calculate_total_price(self, x, y):
        return x * y 

# python passes an object/instance of a class to the method as an argume-
# when that method is called. In other words, self refers to the object
# from which the method is called.

item1 = Item() # create an object/instance of class Item.
item1.name = 'Phone' 
# Go into instance, item1, and put 'Phone' in attribute/member variable/
# field of class, Item, or its instance, item1.
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))
# Go inside the instance/object, item1, and call the function, calculate_total_
# price(), and pass the object, item1, as the argument for self, and evaluate 
# item1.price and item1.quanity to 100 and 5, respectively, and pass them as 
# arguments for x and y, respectively, to the function.

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

print(type(item1)) # datatype Item
print(type(item1.name)) # datatype, str.
print(type(item1.price)) # datatype, int.
print(type(item1.quantity)) # datatype, int.
# An object of a class, item1, has the user defined datatype, Item. Rest
# of the attributes of class or its object such as names, price etc have
# the original primitive datatypes like str, and int etc.


