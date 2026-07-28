#BAI01 : 
# Nhap chuoi
s = input("Nhap chuoi : ")
# 1. Dao nguoc chuoi
dao_nguoc = ""
for i in range(len(s) - 1, -1, -1):
    dao_nguoc += s[i]
print("Chuoi dao nguoc : ", dao_nguoc)
# 2. Sapxep cac ky tu
ds = list(s)
ds.sort()
chuoi_sap_xep = ""
for ky_tu in ds:
    chuoi_sap_xep += ky_tu
print("Chuoi sau khi sap xep la : ", chuoi_sap_xep)
# 3. Ktra chuoi doi xung 
if s == dao_nguoc:
    print("Day la chuoi doi xung!")
else:
    print("Day khong phai la chuoi doi xung!")
# 4. Tim ky tu xuat hien nhieu nhat
tap_ky_tu = set(s)
max_dem = 0
for ky_tu in tap_ky_tu:
    if s.count(ky_tu) > max_dem:
        max_dem = s.count(ky_tu)
ket_qua = []
for ky_tu in tap_ky_tu:
    if s.count(ky_tu) == max_dem:
        ket_qua.append(ky_tu)
ket_qua.sort()
print("Ky tu xuat hien nhieu nhat :")
for ky_tu in ket_qua:
    print(ky_tu, end=" ")
print()
print("So lan xuat hien", max_dem)
# 5. Kiem tra du 5 nguyen am : 
chuoi_thuong = s.lower()
if "a" in chuoi_thuong and "e" in chuoi_thuong and "i" in chuoi_thuong and "o" in chuoi_thuong and "u" in chuoi_thuong:
    print("Chuoi chua day du 5 nguyen am Tieng Anh!")
else:
    print("Chuoi khong chua day du 5 nguyen am Tieng Anh!")


#BAI02 : 
# Nhap du lieu
input1 = input("Nhap cac san pham: ")
input2 = input("Nhap san pham can kiem tra: ")
# Tao list va chuan hoa
ds = input1.split(",")
for i in range(len(ds)):
    ds[i] = ds[i].strip().title()
print("Danh sach san pham:")
print(ds)
# Tong so san pham
print("Tong so san pham da mua:", len(ds))
# San pham o vi tri giua
if len(ds) % 2 != 0:
    print("San pham o vi tri giua:", ds[len(ds) // 2])
# Tim san pham mua nhieu nhat
tap_san_pham = set(ds)
max_dem = 0
for san_pham in tap_san_pham:
    if ds.count(san_pham) > max_dem:
        max_dem = ds.count(san_pham)
ket_qua = []
for san_pham in tap_san_pham:
    if ds.count(san_pham) == max_dem:
        ket_qua.append(san_pham)
ket_qua.sort()
print("Cac san pham duoc mua nhieu nhat:")
for san_pham in ket_qua:
    print(san_pham + ":", max_dem, "lan")
# Kiem tra san pham can tim
input2 = input2.strip().title()
if input2 in ds:
    print(input2, "da duoc mua", ds.count(input2), "lan.")
else:
    print(input2, "chua duoc mua.")
# Cap nhat danh sach
ds.insert(0, "Banh Nabati")
if "Sua" in ds:
    ds.remove("Sua")
print("Danh sach sau khi cap nhat:")
print(ds)

#BAI03 : 
# Nhap du lieu
input1 = input("Nhap so thich cua nguoi A: ")
input2 = input("Nhap so thich cua nguoi B: ")
# Tao list va chuan hoa
ds_a = input1.split(",")
ds_b = input2.split(",")
for i in range(len(ds_a)):
    ds_a[i] = ds_a[i].strip().title()
for i in range(len(ds_b)):
    ds_b[i] = ds_b[i].strip().title()
# Chuyen sang set
set_a = set(ds_a)
set_b = set(ds_b)
print("Cac so thich cua nguoi A:")
print(set_a)
print("Cac so thich cua nguoi B:")
print(set_b)
# So thich chung
so_thich_chung = set_a & set_b
print("So thich chung:")
if len(so_thich_chung) == 0:
    print("Khong co so thich chung.")
else:
    print(so_thich_chung)
# So thich chi nguoi A co
print("So thich chi nguoi A co:")
print(set_a - set_b)
# Tat ca so thich
print("Tat ca so thich:")
print(set_a | set_b)
# Do tuong dong
tong_so_thich = set_a | set_b
if len(tong_so_thich) == 0:
    do_tuong_dong = 0
else:
    do_tuong_dong = len(so_thich_chung) / len(tong_so_thich) * 100
print("Do tuong dong: %.2f%%" % do_tuong_dong)

#BAI04 : 
# Nhap so luong khoan chi
n = int(input("Nhap so luong khoan chi: "))
ds = []
# Nhap cac khoan chi
for i in range(n):
    du_lieu = input().split(",")
    ten = du_lieu[0].strip().title()
    so_tien = int(du_lieu[1].strip())
    danh_muc = du_lieu[2].strip().title()
    khoan_chi = (ten, so_tien, danh_muc)
    ds.append(khoan_chi)
# In danh sach
print("Danh sach cac khoan chi:")
for khoan_chi in ds:
    print(khoan_chi)
# Tong chi tieu
tong = 0
for khoan_chi in ds:
    tong += khoan_chi[1]
print("Tong chi tieu:", tong, "VND")
# Thong ke theo danh muc
print("Thong ke theo danh muc:")
tap_danh_muc = set()
for khoan_chi in ds:
    tap_danh_muc.add(khoan_chi[2])
for danh_muc in tap_danh_muc:
    so_khoan = 0
    tong_tien = 0
    for khoan_chi in ds:
        if khoan_chi[2] == danh_muc:
            so_khoan += 1
            tong_tien += khoan_chi[1]
    print(danh_muc + ":")
    print("- So khoan chi:", so_khoan)
    print("- Tong tien:", tong_tien, "VND")
# Kiem tra vuot muc chi tieu
if tong > 5000000:
    print("Tong chi tieu vuot qua 5000000 VND.")
# Tim khoan chi lon nhat
lon_nhat = ds[0]
for khoan_chi in ds:
    if khoan_chi[1] > lon_nhat[1]:
        lon_nhat = khoan_chi
print("Khoan chi co so tien lon nhat:")
print(lon_nhat)