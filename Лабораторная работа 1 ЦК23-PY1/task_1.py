numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
one = len(numbers)
sum_numbers = sum(numbers[0:4]) + sum(numbers[5:21])
average_number = sum_numbers / one
numbers[4] = average_number
print("Измененный список:", numbers)
