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
chuyen_doi_nhiet_do = lambda c: c * 9 / 5 + 32
c = float(input("Nhap nhiet do C: "))
print(chuyen_doi_nhiet_do(c))
kiem_tra_chan_le = lambda x: "chan" if x % 2 == 0 else "le"
so = int(input("Nhap so: "))
print(kiem_tra_chan_le(so))
tinh_tien_tip = lambda hoa_don, phan_tram: hoa_don * phan_tram / 100
hoa_don = float(input("Nhap hoa don: "))
phan_tram = float(input("Nhap phan tram tip: "))
print("So tien tip:", tinh_tien_tip(hoa_don, phan_tram))
rut_gon_ten = lambda ten: ten.upper()
ten = input("Nhap ho va ten: ")
print(rut_gon_ten(ten))

#BAI03 :
san_pham = [
    {"ma_sp": "SP01", "ten_sp": "laptop", "danh_muc": "dien tu", "gia": 15000000, "ton_kho": 5},
    {"ma_sp": "SP02", "ten_sp": "chuot", "danh_muc": "dien tu", "gia": 300000, "ton_kho": 0},
    {"ma_sp": "SP03", "ten_sp": "ban", "danh_muc": "noi that", "gia": 2000000, "ton_kho": 2},
    {"ma_sp": "SP04", "ten_sp": "ghe", "danh_muc": "noi that", "gia": 800000, "ton_kho": 0}
]
dien_tu = list(filter(lambda sp: sp["danh_muc"] == "dien tu", san_pham))
het_hang = list(filter(lambda sp: sp["ton_kho"] == 0, san_pham))
ten_san_pham = list(map(lambda sp: sp["ten_sp"], san_pham))
san_pham_cao_cap = list(filter(lambda sp: sp["gia"] >= 1000000, san_pham))
khuyen_mai = list(map(lambda sp: "Tang voucher 100k cho khach mua " + sp["ten_sp"], san_pham_cao_cap))
print("San pham dien tu:")
print(dien_tu)
print("San pham het hang:")
print(het_hang)
print("Ten cac san pham:")
print(ten_san_pham)
print("Khuyen mai:")
print(khuyen_mai)

#BAI04 :
danh_sach_hoc_sinh = [
    {"ten": "Nguyen Van A", "diem": {"Toan": 9, "Van": 6, "Anh": 9}},
    {"ten": "Tran Thi B", "diem": {"Toan": 8, "Van": 7, "Anh": 9}},
    {"ten": "Le Van C", "diem": {"Toan": 9, "Van": 8, "Anh": 8}},
    {"ten": "Pham Thi D", "diem": {"Toan": 6, "Van": 5, "Anh": 7}}
]
sap_xep_toan = sorted(
    danh_sach_hoc_sinh,
    key=lambda hs: hs["diem"]["Toan"],
    reverse=True
)
print("Yeu cau 1:")
for hs in sap_xep_toan:
    print(hs["ten"])
anh_cao_nhat = max(
    danh_sach_hoc_sinh,
    key=lambda hs: hs["diem"]["Anh"]
)
print("Yeu cau 2:")
print(anh_cao_nhat["ten"])
sap_xep_tong = sorted(
    danh_sach_hoc_sinh,
    key=lambda hs: (-sum(hs["diem"].values()), hs["ten"])
)
print("Yeu cau 3:")
for hs in sap_xep_tong:
    print(hs["ten"])
hoc_sinh_gioi = list(
    filter(
        lambda hs: sum(hs["diem"].values()) >= 24,
        danh_sach_hoc_sinh
    )
)
hoc_sinh_gioi = sorted(
    hoc_sinh_gioi,
    key=lambda hs: sum(hs["diem"].values()),
    reverse=True
)
ten_hoc_sinh_gioi = list(
    map(
        lambda hs: hs["ten"],
        hoc_sinh_gioi
    )
)
print("Yeu cau 4:")
print(ten_hoc_sinh_gioi)