import os

directory = "test_cases_4/CZE/0002_in.txt"
file_path = os.path.join("Ulohy", directory)

try:
    with open(file_path, "r") as file:
        lines = file.readlines()

    list_of_numbers = []
    for line in lines:
        numbers = line.strip().split()
        for number in numbers:
            try:
                num = int(number)
                if num < -1000 or num > 1000:
                    raise ValueError("Input value is not within the valid range.")
                list_of_numbers.append(num)
            except ValueError:
                print(f"Error: '{number}' is not a valid integer.")

    if len(list_of_numbers) == 0:
        raise ValueError("Input sequence is empty.")

    if len(list_of_numbers) > 2000:
        raise ValueError("Input sequence is too long (over 2000 numbers).")

    list_of_sums = []
    number_of_pairs = 0

    for i in range(len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers)):
            temp_sum = sum(list_of_numbers[i:j + 1])
            list_of_sums.append(temp_sum)
            print(temp_sum)

    print("------")
    for i in range(len(list_of_sums)):
        for j in range(i + 1, len(list_of_sums)):
            if list_of_sums[i] == list_of_sums[j]:
                number_of_pairs += 1
                continue

    print(number_of_pairs)

except FileNotFoundError:
    print("Error: File not found.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
