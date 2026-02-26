def remove_odd(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list
# chương trình chính
numbers = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    x = int(input("Nhập số: "))
    numbers.append(x)
even_numbers = remove_odd(numbers)
print("Danh sách ban đầu:", numbers)
print("Danh sách sau khi bỏ số lẻ:", even_numbers)