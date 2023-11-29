#1
my_list = [1, 2, 3, 4, 5]
index_to_replace = int(input("Введіть індекс для заміни: "))
new_value = int(input("Введіть нове число: "))
my_list[index_to_replace] = new_value
my_list.pop()
print("Довжина списку:", len(my_list))
print("Оновлений список:", my_list)
#2
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Не відсортований список:", my_list)
bubble_sort(my_list)
print("Відсортований список:", my_list)
#3
def remove_duplicates(arr):
    unique_list = []
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Список з дублікатами:", my_list)
unique_list = remove_duplicates(my_list)
print("Список без дублікатів:", unique_list)
#4
chess_board = [["_" for _ in range(8)] for _ in range(8)]

chess_board[0][0] = "T"
chess_board[0][7] = "T"
chess_board[7][0] = "T"
chess_board[7][7] = "T"
for row in chess_board:
    print(" ".join(row))
