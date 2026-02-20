#to print 1 to 100 using while loop
'''num = 1
while num < 100:
    num += 1
    print(num)'''

#even num bw 10-41
'''num = 10
while num <= 41:
    if num % 2 == 0:
        print(num)
    num += 1'''

# odd num bw 1 - 50
'''num = 1
while num <= 50:
    if num%2 !=0:
        print(num)
    num +=1'''

#even or odd from the list
'''numbers = [10, 15, 22, 33, 40, 55]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i], "is Even")
    else:
        print(numbers[i], "is Odd")
    i += 1'''

#sum of even numbers up to n
n = int(input("Enter a number: "))
num = 1
total = 0
while num <= n:
    if num % 2 == 0:
        total += num
    num += 1
print("Sum of even numbers up to", n, "is:", total)

    
