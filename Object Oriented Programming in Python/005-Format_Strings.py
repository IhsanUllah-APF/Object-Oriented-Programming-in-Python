# Bismillah

# Format Strings

from datetime import datetime # for the date - see end of the file.

first_name = 'Corey'
last_name = 'Scheffer'

# print(f'My first name is {first_name} and the last name is {last_name}') 
# # space gets printed between between the two {}. 

# print(f'{first_name.upper()} {last_name.upper()}') # to capatilize the first and last names.

person = {'name': 'Jenn', 'age': 23} # dictionary two key-value pairs. Strings enclosed in ''.

sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)
# it's calling format function on all the content before dot oeprator. The argument of the function, format, takes
# name of the dictionary, person, and then names of the keys, name and age, in string. person['name'] evaluates to
# Jenn and person ['age'] evaluates to 23. Also, note that [] have been used to access the values of keys from the
# dictionary, person.

#sentence = f'My name is {person['name']} and I am {person['age']} years old'
# will give error since the first single ' and the second single ' before name in [] are taken only complete string.
# The way to escape this confusion for Python is to use double quotes at the end and start as:  

sentence = f"My first name is {person['name']} and I am {person['age']} years old." 
# print(sentence) 
# now there is no error. Also, () and {} around 'name' and 'age' gives error. So, using [] is must.


calculation = f'Four times elevent is {4 * 11}'
#print(calculation)
# expressions can be called within {} in f string.

for i in range (1, 11):
    sentence = f'the value is {i:02}' # will evaluate the i to the number and save the whole string in variable, sentence.
    #print(sentence)
# so fstring can be used in loops as well. Also, :02 for two digits.

pi = 3.14159265
sentence = f'pi is equal to {pi}'
#print(sentence)
sentence = f'pi is equal to {pi:.4f}' # .4 for printing upto 4 digits after decimal and f stands for floating point.
#print(sentence)

birthday = datetime(1990, 1, 1)
sentence = f'Jenn has a birthday on {birthday}'
print(sentence)

sentence = f'Jenn has a birthday on {birthday: %B %d, %Y}' 
print(sentence)
# %B %d and %Y for full month (Janaury), date and year, respectively to look like (January 01, 1990).

# REMEMBER to use f'...{}..' rather than f'...{} {}.format()' since in the second case we have to remember and figure
# out which value corresponds to which place-holder.











