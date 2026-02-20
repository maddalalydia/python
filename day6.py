#to find the sum of even numbers b/w the range of n and m
'''n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
total = 0
while n <= m:
    if n % 2 == 0:
        total += n
    n += 1
print("Sum of even numbers:", total)'''

#model 2
'''n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
total = 0
if n%2!=0:
    n=n+1
while n <= m:
    if n % 2 == 0:
        total += n
    n += 2 #where it decreases the no of steps
print("Sum of even numbers:", total)'''

#find the length of  numbers
#sum of digits in a number
#reverse of a num
#check weather the num is palindrome or not
#check weather the num is armstrong or not
#perfect num

#find the length of  numbers
'''num = input("Enter a number: ")
length = len(num)
print("Length of number:", length)'''
#model 2
'''num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Length of number:", count)'''

#sum of digits in a number
'''num = int(input("Enter a number: "))
total = 0
while num > 0:
    i = num % 10
    total += i
    num //= 10
print("Sum of digits:", total)'''

#reverse of a num
'''num = int(input("Enter a number: "))
r = 0
while num > 0:
    digit = num % 10
    r = r * 10 + digit
    num //= 10
print("Reversed number:", r)'''

#check weather the num is palindrome or not
'''num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")'''

#check weather the num is armstrong or not

#perfect num
n = int(input())
original = n
i = 1
total = 0
while i <= n // 2:
    if n % i == 0:
        total += i
    i += 1
if total == original:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#model 2
'''n = int(input())
i = 1
total = 0
while i < n:
    if n % ib == 0:
        total += i
    i += 1
if total == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")'''




