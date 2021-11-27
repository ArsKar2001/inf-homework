import random

arr = [random.randint(0, 100) for i in range(10)]
print(arr)
n = int(input("Введите число: "))
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j and arr[i] + arr[j] == n:
            print(arr[i], " + ", arr[j], ' = ', n)
