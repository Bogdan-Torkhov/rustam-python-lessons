def Add(first_number, second_number):
    return first_number + second_number


def Subtract(first_number, second_number):
    return first_number - second_number


def Multiply(first_number, second_number):
    return first_number * second_number


def Divide(first_number, second_number):
    return first_number * second_number


print("Select operator:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == '1':
            print(first_number, "+", second_number,
                  "=", Add(first_number, second_number))

        elif choice == '2':
            print(first_number, "-", second_number, "=",
                  Subtract(first_number, second_number))

        elif choice == '3':
            print(first_number, "*", second_number, "=",
                  Multiply(first_number, second_number))

        elif choice == '4':
            print(first_number, "/", second_number, "=",
                  Divide(first_number, second_number))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
