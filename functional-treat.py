print("Welcome to the Data Analyzer and Transformer Program\n")
array_1d = []
while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary ")
    print("3. Calculate Factorial ")
    print("4. Filter Data by Threshold ")
    print("5. Sort Data")
    print("6. Display Dataset Statistics  ")
    print("7. Exit program")
    choice = int(input("Enter your choice:"))
    match choice:
        case 1:
            user_input = input("Enter data for a 1D array (separated by spaces): ")
            string_list = user_input.split()
            for item in string_list:
                number = int(item)
                array_1d.append(number)
            print("Data has been stored successfully!")      
        case 2:
            array_length = len(array_1d)
            array_min = min(array_1d)
            array_max = max(array_1d)
            array_sum = sum(array_1d)
            print("\nData Summary:")
            print(f"- Total elements: {array_length}")
            print(f"- Minimum value: {array_min}")
            print(f"- Maximum value: {array_max}")
            print(f"- Sum of all values: {array_sum}")
        case 3:
            n = int(input("Enter a number to calculate its factorial: "))
            def factorial(num):
                if num == 0 or num == 1:
                    return 1
                return num * factorial(num - 1)
            print("Factorial of", n, "is:", factorial(n)) 
        case 4:
            threshold = int(input("Enter a threshold value: "))
            result = list(filter(lambda x: x >= threshold, array_1d))
            print("Filtered Data (values >=", threshold, "):")
            print(*result)
        case 5:
            print("Choose sorting option: ")
            print("1. Ascending Order")
            print("2. Desending Order") 
            x = int(input("Enter your sorting option numbers: ")) 
            match x:
                case 1:
                    array1d = sorted(array_1d)
                    print("Sorted Data in Ascending order: ")
                    print(*array1d)
                case 2:
                    array1d = sorted(array_1d)
                    print("Sorted Data in Ascending order: ")
                    array = reversed(array1d) 
                    print(*array)
        case 6:
            def statistics(array_1d):
                minimum = min(array_1d)
                maximum = max(array_1d)
                total = sum(array_1d)
                average = total / len(array_1d)
                return minimum, maximum, total, average
            mn, mx, total, avg = statistics(array_1d)
            print("Minimum:", mn)
            print("Maximum:", mx)
            print("Sum:", total)
            print("Average:", round(avg, 2))
        case 7:
            print("Thank you for using the Data Analyzer and Transformer prigram. Goodbye!")
            break   
        case _:
            print("Invalide number try Again please!")   
            break
