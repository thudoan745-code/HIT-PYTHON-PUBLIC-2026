def tinh_tien_thua(gia, tra):
    return tra - gia
gia = int(input("Nhap gia san: "))
tra = int(input("Khach dua: "))
tien_thua = tinh_tien_thua(gia, tra)
menh_gia = [20, 10, 5, 2, 1]
for x in menh_gia:
    so_to = tien_thua // x
    tien_thua = tien_thua % x
    print("So to menh gia ", x, "la:", so_to)