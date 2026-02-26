numbers = []
while True:
    x = input("Nhập một số (enter để dừng): ")
    if x == "":
        break
    numbers.append(int(x))
numbers.sort(reverse=True)
print("5 số lớn nhất là:")
print(numbers[:5])