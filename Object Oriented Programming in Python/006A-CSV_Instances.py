# Bismillah

# Read from CSV file and automatically create objects from the CSV file. Also, Class Vs Static Methods
import csv # import the library, csv, to read etc the cvs file. The lib is imported before start of the class.
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

    @classmethod # a decorator to change the nature of methods.
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
           reader = csv.DictReader(f) # go inside package csv and call a function DictReader which should read the file
           # items.csv accessible through f and put it in the variable, reader.
           items = list(reader) # take the reader from above, and convert it into list and save it in variable, items.
           #print(items) # prints a list of dictionaries where each dictionary is one row in the csv file. We would 
           # get a list of lists where each inner list would one row in the csv file if we use csv.reader(f) rather
           # than csv.DictReader(f) which reads the file converts it into dictionary as well.
        for item in items:
            #print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            ) 
    # self cannot be passed as an argument to this function because self refers to an instance and this method/function
    # is meant to create instance from csv file so at the time of calling this method we do not have an instance. Thus,
    # self cannot be passed as argument to this method. The solution is to make this method a class method.
    # The class method can be accessed from the class level only.
    # the default argument, cls, means that the class reference must be passed as a first argument. In our example, 
    # class, Item, will be passed as a first argument.
    # print(item) in the for loop returns dictionaries for each row taking the titles from the first row. Each value
    # in all the dictionaries is string.

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv() # the class method/function is to be called from here and then the
# whole process of executing this method will be started.

print(Item.all)
# print(dir(csv)) # to find the tasks one can do with CSV library.
# print(dir(Item)) # to find what can be done in class, Item.

# Start from 1:03