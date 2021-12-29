# Bismillah

# currently, we cannot print all the objects, alongwith their attributes, of the class that we have created so with 
# one command. For this purpose, we need to have a list of 5 elements, where each element is an instance/object of 
# the class. So, let's create such a list.

class Item:

    pay_rate = 0.8 
    
    all = [] # an empty list, which is global or class attribute.
    
    def __init__(self, name: str, price: float, quantity = 0): 
                
        # Run validations to the received arguments.
        assert price >= 0, f'Price {price} is not equal to or greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not equal to or greater than zero!'

        # Assignment to an object.
        self.name = name
        self.price = price
        self.quantity = quantity

        # Put the instances in the list, all.
        Item.all.append(self) # Item.all will get us to the list and append will put in the value 'self' in it which
        # is the instance itself.

    def calculate_total_price(self): 
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity})"

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

# print(Item.all) # the list is produced here without the magic function, repr() or str(), which is not meaningful, as:
# " [<__main__.Item object at 0x0000016F56532EC0>, <__main__.Item object at 0x0000016F56530550>, 
# <__main__.Item object at 0x0000016F565304F0>, <__main__.Item object at 0x0000016F565303D0>,
# <__main__.Item object at 0x0000016F565320B0>]". But note that the list contains 5 elements, one for each instance
# that we have created so far. To make instances more descriptive and meaningful, we need to use magic function/methods
# such as str() or repr(). So, let's us define one of them above.

print(Item.all) # Now instead of the same print function producing the above meaningful list of instances, it produces
# this meaningful list as "[item(Phone, 100, 5, item(Laptop, 1000, 3, item(Cable, 10, 5, item(Mouse, 50, 5, 
# item(Keyboard, 75, 5]". We can perform any eligible operation on this list on as:

#print(Item.all[1]) # it will produce the zeroth element of the list, which is the first object of the class.

for instance in Item.all: # it will take each element one by one from the list, Item.all, and put it in variable, 
    print(instance.name) # instance. Now, in variable, instance, name will be searched and evaluated and its value will
    # be printed. for loop seems intillegent enough to know which value in the element is name based on the working
    # repr(). The same output can be produced after append() and before repr(), which means once the list contains
    # the items, even we see strange description, but still different attributes of objects such as names etc can
    # be obtained.
