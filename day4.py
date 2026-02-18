# to check weather the num is even -ve even odd and -ve odd
'''num = int(input())
if(num >=0 and num %2==0):
     print("the number is positive even")
elif(num<0and num %2 == 0 ):
    print("num is -ve even")
elif(num>=0 and num %2 !=0):
    print("the number is odd")
else:
    print("the number is -ve odd")'''

# to find the gratest of 3 numbers
'''numbers = list(map(int, input("Enter three numbers : ").split()))
print("Greatest number is:", max(numbers))'''

# least num among the 3 mum
'''numbers = list(map(int, input("Enter three number: ").split()))
print("least number is:", min(numbers))'''
#same
'''n1,n2,n3=map(int,input().split())
if(n1>n2 and n1>n3):
    print("n1 is big")
elif(n2>n3):
    print("n2 is big")
else:
    print("n3 is big")'''

#nested if elif(+ev -ev ,+odd -odd)
n= int(input())
if(n>=0):
    if(n%2==0):
        print("+ve even")
    else:
        print("+ve odd")
else:
    if(n%2==0):
        print("-ve even")
    else:
        print("-ve odd")
    


