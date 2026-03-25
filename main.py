# import modules
from addition import add
import sub
from division import div as division
import multiplication as mul
# main function
if __name__ == "__main__":
    print("Welcome to small calculator")
    while True:
        print("Please select an operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            a,b = map(int, input("Enter two numbers to add: ").split())
            print(add(x=a, y=b))
        elif choice == 2:
            a,b = map(int, input("Enter two numbers to subtract: ").split())
            print(sub.sub(x=a, y=b))
        elif choice == 3:
            a,b = map(int, input("Enter two numbers to multiply: ").split())
            print(multiplication.mul(x=a, y=b))
        elif choice == 4:
            a,b = map(int, input("Enter two numbers to divide: ").split())
            print(division(x=a, y=b))
        elif choice == 5:
            exit()
        else:
            print("Invalid choice.")

