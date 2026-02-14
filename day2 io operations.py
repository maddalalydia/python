'''#read input numbers from user
num = input()
print(type(num)) #checking the type of numb
print(num)'''

'''#implicit type conversion
num1 = int(input())
val = float(input())
print(type(num1), type(val)) #checking the type of numb
res = num1+val
print(res)'''

'''num1 = input()
print(type(num1)) #checking the type of numb
res =int(num1) + 10
print(res)'''

'''num1 = input()
print(type(num1)) #checking the type of numb
res =num1 + 10
print(res)
#it get error to over come add int in res'''

'''num1 = input()
print(type(num1)) #checking the type of numb
res =int(num1) + 10
print(res)'''

'''#converting int to float, string to bool
num = 12
print(float(num))
print(str(num))
print(bool(num))'''

num1 = 10.75   # float value

print(type(num1))   # checking the type of num1

# Float to int
num_int = int(num1)
print(num_int)
print(type(num_int))

# Float to tuple
num_tuple = (num1,)   # converting float into tuple
print(num_tuple)
print(type(num_tuple))

# Float to string
num_str = str(num1)
print(num_str)
print(type(num_str))

# Performing addition (like your example)
res = num1 + 10
print(res)

