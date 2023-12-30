###########################################
# Escape Sequences
# \ is used to inform python that next character is to be treated like a STRING

ex1 = 'Saksham \'Dutt'
ex2 = 'Saksham \nDutt' # \n - Newline Character

##########################################
# Formatted String
first = 'Saksham'
last = 'Dutt'

# print(f"{first} {last} {len(first)}")

# UPPER - To capatalise all letters of the words
# LOWER - To lower all the letters of the words
# TITLE - To make it like 'Saksham Dutt'
# STRIP - To remove all whitespaces  from beginning and end of the strings
# FIND() - To check the availabilty of any keyword in the string (-1 if not exit// 0 if exist )



# NUMERIC OPERATORS 
# https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp

# TYPE COERSION FUNCTIONS
# int/float/str for conversions

#bool(O) = false bool(any other number than zero) = true

age =22
message = 'Eligible' if age >= 18 else 'Not Eligible' # TERNARY OPERATOR

# Example of cleaner if code
# 18 <= age < 65:

high_income = False
good_credit = True
scale = False
# if high_income and good_credit and scale:# Code execute from left to right as soon as it finds out that high income is false code short circuit it doesn't matter wht other parameters are
#     print('OKAY')


#----------------------------------------------
    
# print(type(range(5)))    
    
# While Loop
command = ''
# while command.lower() != 'quit':
#     command = input('>')
#     print('Echo', command)            

# FUNCTIONS
'''
def multiply(*numbers):#*numbers make tuple of arguments
    result = 1
    for number in numbers:
        result *= number
    return result    
print(multiply(2,3,4,5))    

'''

'''
def save_user(**user):#RETURN DICTIONARY
    print(user)

save_user(id=1,name='John')# When we use double astericks ,we should send key value pairs in arguments.    

'''


# CONCATINATION OF LIST
# zeroes = [0] * 5
# LIST = list1 + list2
numbers = list(range(20)) # List() takes any interable as arguement 
char = list('Hello World')


# LIST UNPACKING
numbers = [1,2,3,4,5]
first,second,third,*other = numbers

# ENUMERATE FUNCTION FOR LOOPING
letters = ['a','b','c']
# for index in enumerate(letters): # return tuple (index,value)
    #  print(index)

'''
(0, 'a')
(1, 'b')
(2, 'c')
'''    

# Add
# append(item) (add at last)
# pop(index) (remove last item) It can index value as arguement to remove item
# del [0:2] delete range of items
# remove(item)
# insert(index, item)

# index function to find index of element
# count give occurance of item in list

numbers = [1,5,12,3]
# numbers.sort(reverse=True)
# print(numbers) # OUTPUT [12, 5, 3, 1]
# print(sorted(numbers)) # sorted(numbers, reverse=True)


#_---------------------------------


items = [
    ('Product1', 10),
    ('Product2', 9),    
    ('Product3', 12)
]

def sort_item(item):
    return item[1]
    
#items.sort(key=sort_item) # When sorting python will get each item in items and send it to sort_item function

# LAMBDA FUNCTIONS
# items.sort(key=lambda item:item[1])#(parameter/expression)
# print(items)

#MAP FUNCTION
# prices= list(map(lambda item: item[1], items))# Returns Map Object
# print(prices) # [10, 9, 12]

x= list(filter(lambda item: item[1] >= 10, items))
# print(x) # [('Product1', 10), ('Product3', 12)]


# List Comprehensions
prices = [item[1] for item in items] # mapping

filtering = [item for item in items if item[1] >= 10] # filtering

# ZIPPING FUNCTIONS
list1 = [1,2,3]
list2 = [10,20,30]

# print(list(zip(list1,list2,'abc'))) # [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]
# Zip also return zipped object(iterable object)

#DICTIONARY COMPREHENSIONS
values = {x:x*3 for x in range(5)}
# print(values)


sentence = 'This is a common interview question'
'''
char_dic = {}
word_list = sentence.split()
print(word_list)

for word in word_list:
    for alpha in word:
        if alpha not in char_dic.keys():
            char_dic[alpha] = 1 
        else:
            char_dic[alpha] +=1

maximum = 0
for i in char_dic.values():
    if maximum < i:
        maximum = i

print(maximum)
index = list(char_dic.values()).index(maximum)
print(list(char_dic.keys())[index],'is maximum repeated ',maximum, 'times.')'''

from pprint import pprint

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1    

# pprint(char_frequency,width=1)        

print(sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True))        

#------------------------------------------
# EXCEPTIONS
try:
    age = int(input("Age: "))
except ValueError as ex:
    print('you don\'t enter a valid age')
    print(ex)
else:
    print('No exceptions were thrown.')       
print('Exection continues')    