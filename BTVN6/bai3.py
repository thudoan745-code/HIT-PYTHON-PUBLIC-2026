import numpy as np

doanh_thu = np.array([35, 42, 89, 125, 50, 80, 120, 200, 150, 220, 300, 450])

doanh_thu_quy = doanh_thu.reshape(4, 3)

print("Cau truc moi: Shape", doanh_thu_quy.shape, "| Ndim:", doanh_thu_quy.ndim)

print("---")

trung_binh = np.mean(doanh_thu_quy, axis=1)
cao_nhat = np.max(doanh_thu_quy, axis=1)

print("Bao cao theo Quy:")
print("Doanh thu trung binh moi Quy:", trung_binh)
print("Thang cao nhat trong moi Quy:", cao_nhat)

print("---")

ket_qua = doanh_thu[(doanh_thu > 80) & (doanh_thu <= 200)]

print("Cac thang thoa man dieu kien (80 < x <= 200):")
print(ket_qua)

print("---")

marketing = np.array([10, 15, 20, 30])

marketing = marketing.reshape(4, 1)

bao_cao = np.hstack((doanh_thu_quy, marketing))

print("Bang bao cao sau khi tich hop chi phi Marketing:")
print(bao_cao)