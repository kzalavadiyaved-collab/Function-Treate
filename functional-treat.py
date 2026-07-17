print("Welcome to the Data Analyzer and Transformer Program\n")

array_1d = []

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    match choice:

        case 1:
            user_input = input("Enter data for a 1D array (separated by spaces): ")
            array_1d = list(map(int, user_input.split()))
            print("Data has been stored successfully!")

        case 2:
            if not array_1d:
                print("No data available. Please input data first.")
                continue

            print("\nData Summary:")
            print("Total elements:", len(array_1d))
            print("Minimum value:", min(array_1d))
            print("Maximum value:", max(array_1d))
            print("Sum of all values:", sum(array_1d))

        case 3:
            n = int(input("Enter a number to calculate its factorial: "))

            def factorial(num):
                if num == 0 or num == 1:
                    return 1
                return num * factorial(num - 1)

            print("Factorial of", n, "is:", factorial(n))

        case 4:
            if not array_1d:
                print("No data available. Please input data first.")
                continue

            threshold = int(input("Enter a threshold value: "))
            result = list(filter(lambda x: x >= threshold, array_1d))

            print("Filtered Data:")
            print(*result)

        case 5:
            if not array_1d:
                print("No data available. Please input data first.")
                continue

            print("1. Ascending Order")
            print("2. Descending Order")

            x = int(input("Enter your sorting option: "))

            match x:
                case 1:
                    print("Sorted Data in Ascending Order:")
                    print(*sorted(array_1d))

                case 2:
                    print("Sorted Data in Descending Order:")
                    print(*sorted(array_1d, reverse=True))

                case _:
                    print("Invalid sorting option!")

        case 6:
            if not array_1d:
                print("No data available. Please input data first.")
                continue

            def statistics(data):
                return min(data), max(data), sum(data), sum(data) / len(data)

            mn, mx, total, avg = statistics(array_1d)

            print("Minimum:", mn)
            print("Maximum:", mx)
            print("Sum:", total)
            print("Average:", round(avg, 2))

        case 7:
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please try again.")
