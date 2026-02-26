n = int(input("Nhập một số nguyên: "))
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")