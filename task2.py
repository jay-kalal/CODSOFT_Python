# # Task 2 : Calculator 
# Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.




def operation_choice(a,b):
    print("1-> Addition")
    print("2-> Subtraction")
    print("3-> Division")
    print("4-> Multiplication")
    print("5-> Floor Division")
    print("6-> Modulus")
    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1: return a+b
        case 2: return a-b
        case 3: return a/b
        case 4: return a*b
        case 5: return a//b
        case 6: return a%b

if __name__ == "__main__":
    no1 = int(input("Enter the no1: "))
    no2 = int(input("Enter the no2: "))
    answer = operation_choice(no1,no2)
    print("The Answer is",answer)
