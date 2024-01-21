matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

for i in range(0, len(matrix), 2):
    row = matrix[i]
    average = sum(row) / len(row)
    print(f"Ср арифметическое элементов строки: {average}")