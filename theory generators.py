####
'''
class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [1,2,3,4,5]
my_iter = MyIterator(my_list)
for num in my_iter:
    print(num)
'''

####
'''
my_list = [1,2,3,4,5]

iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
'''

####
'''
def my_generator(data):
    for i in data:
        yield i

my_list = [1,2,3,4,5]
my_gen = my_generator(my_list)
for num in my_gen:
    print(num)
'''

####

def number_generator(n):
    for i in range(n):
        yield i

generator = number_generator(5)
for num in generator:
    print(num)


####

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)


####
