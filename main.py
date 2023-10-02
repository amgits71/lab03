def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Введите количество чисел: "))
arr = []

for _ in range(n):
    num = int(input(f"Введите {_+1}-е число: "))
    arr.append(num)

bubble_sort(arr)

print("Отсортированный список:")
print(arr)