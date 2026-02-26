def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total
numbers = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    x = int(input("Nhập số: "))
    numbers.append(x)
result = sum_list(numbers)
print("Tổng các số là:", result)