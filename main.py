def bubble_sort(arr, is_ascending):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if not is_ascending:
        arr.reverse()

n = int(input("Введите количество чисел: "))
arr = []

for _ in range(n):
    num = int(input(f"Введите {_+1}-е число: "))
    arr.append(num)

is_ascending = input("Сортировать по возрастанию (да/нет)? ").lower() == "да"
bubble_sort(arr, is_ascending)

print("Отсортированный список:")
print(arr)

