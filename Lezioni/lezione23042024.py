def substract(a,b):
    res=a-b
    return res
my_result=(substract(4,1))
print(my_result)

my_list: list=[index for index in range(100)]
print(my_list)# questa è una list comprehension


my_list2: list=[index if index %2==0 else -1 for index in range(100)]
print(my_list2)