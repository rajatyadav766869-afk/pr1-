# #Logic box=
# print("Welcome to the Pattern Generator and Number Analyzer!")
# print("1. Generate a pattern")
# print("2. Analyze a range of numbers")
# print("3. Exit")

# #try=
# option = int(input("Select an option (1, 2, or 3): "))
# print("Invalid input. Please enter a numbe1r (1, 2, or 3).")
# exit()

# if option == 1:
#     print("\nPattern Generator")
#     try:
#         row = int(input("Enter the number of rows: "))
#         if row <= 0:
#             print("Number of rows must be positive.")
#         else:
#             for i in range(0, row + 1):
#                 print("* " * i)
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# elif option == 2:
#     print("\nNumber Analyzer")
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# if start >= end:
#             print("Start must be less than end.")
# else:
#             for i in range(start, end):
#                 if i % 2 == 1:
#                     print(f"Number {i} is odd")
#                 else:
#                     print(f"Number {i} is even")
#             total = sum(range(start, end))
#             print(f"Sum of all numbers from {start} to {end - 1} is: {total}")
#         print("Invalid input. Please enter valid numbers.")
# elif option == 3:
#     print("Exiting the program. GOODBYE!")
# else:
#     print("Invalid option. Please select 1, 2, or 3.")
print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\n--- Main Menu ---")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    
    option = int(input("Select an option (1, 2, or 3): "))
    
    # print("Invalid input. Please enter a number (1, 2, or 3).")
    # continue

    if option == 1:
        print("\nPattern Generator")
        row = int(input("Enter the number of rows: "))
        if row <= 0:
                print("Number of rows must be positive.")
        else:
                for i in range(1, row + 1):
                    print("* " * i)
                print("Invalid input. Please enter a valid number.")
    elif option == 2:
        print("\nNumber Analyzer:")
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start > end:
                print("Start must be less than or equal to end.")  
        else:
                for i in range(start, end + 1):
                    if i % 2 == 0:
                        print(f"Number {i} is even")
                    else:
                        print(f"Number {i} is odd")
                total = sum(range(start, end + 1))
                print(f"Sum of all numbers from {start} to {end} is: {total}")
                print("Invalid input. Please enter valid numbers.")

    elif option == 3:
        print("Exiting the program. GOODBYE!")
        break
    else:
        print("Invalid option. Please select 1, 2, or 3.")