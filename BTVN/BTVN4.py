#BAI01: 
def nhap_dict():
    n = int(input("Nhap so luong san pham :  "))
    kho_hang = {}
    for i in range(n):
        ten = input("Nhap ten san pham : ")
        so_luong = int(input("Nhap so luong : "))
        kho_hang[ten] = so_luong
    return kho_hang
def quan_ly_kho_hang(kho_hang, sp_moi, sp_xoa):
    so_luong_laptop = kho_hang.get("Laptop", 0)
    print("So luong laptop ban dau la :", so_luong_laptop)
    kho_hang.update(sp_moi)
    ket_qua = kho_hang.pop(sp_xoa, "Khong ton tai")
    print("Ket qua xoa :", ket_qua)
    print("Cac san pham hien co:")
    for ten in kho_hang.keys():
        print(ten)
    tong = sum(kho_hang.values())
    return tong
print("Nhap kho hang ban dau : ")
kho_hang = nhap_dict()
print("Nhap hang moi")
sp_moi = nhap_dict()
sp_xoa = input("Nhap ten san pham can xoa : ")
tong = quan_ly_kho_hang(kho_hang, sp_moi, sp_xoa)
print("Tong so luong hang trong kho", tong)

#BAI02 : 
