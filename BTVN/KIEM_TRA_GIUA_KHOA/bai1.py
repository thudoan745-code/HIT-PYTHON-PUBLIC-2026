x = int(input("Nhap x: "))
a = list(map(int, input("Nhap cac he so: ").split()))
bac = len(a) - 1
tong = 0
for i in range(len(a)):
    tong += a[i] * (x ** bac)
    bac -= 1
print("Gia tri da thuc la:", tong)
