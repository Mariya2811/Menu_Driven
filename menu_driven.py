def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)

def factorial():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial not defined for negative numbers.")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print("Factorial:", result)

def even_or_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def reverse_string():
    s = input("Enter a string: ")
    print("Reversed string:", s[::-1])

def is_prime():
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not a prime number.")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not a prime number.")
            return
    print("It is a prime number.")

def main():
    while True:
        print("\n----- MENU -----")
        print("1. Add two numbers")
        print("2. Factorial of a number")
        print("3. Even or Odd")
        print("4. Reverse a string")
        print("5. Check Prime")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_numbers()
        elif choice == '2':
            factorial()
        elif choice == '3':
            even_or_odd()
        elif choice == '4':
            reverse_string()
        elif choice == '5':
            is_prime()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
