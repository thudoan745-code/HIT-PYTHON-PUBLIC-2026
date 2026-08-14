#BAI01:
class Employee:
    def __init__(self, ten, luong, phong_ban):
        self.ten = ten
        self.__luong = luong
        self._phong_ban = phong_ban

    def get_luong(self):
        return self.__luong

    def tang_luong(self, so_tien):
        if so_tien > 0:
            self.__luong += so_tien

    def tinh_thuong(self):
        return self.__luong * 0.05

    def hien_thi_thong_tin(self):
        print("Ten:", self.ten)
        print("Luong:", self.__luong)
        print("Phong ban:", self._phong_ban)
        print("Tien thuong:", self.tinh_thuong())

class Developer(Employee):
    def __init__(self, ten, luong, phong_ban, ngon_ngu_lap_trinh, so_gio_tang_ca):
        super().__init__(ten, luong, phong_ban)
        self.ngon_ngu_lap_trinh = ngon_ngu_lap_trinh
        self.so_gio_tang_ca = so_gio_tang_ca

    def tinh_thuong(self):
        return self.get_luong() * 0.10 + self.so_gio_tang_ca * 100000

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print("Ngon ngu:", self.ngon_ngu_lap_trinh)
        print("So gio tang ca:", self.so_gio_tang_ca)

class Manager(Employee):
    def __init__(self, ten, luong, phong_ban, so_nhan_vien):
        super().__init__(ten, luong, phong_ban)
        self.so_nhan_vien = so_nhan_vien

    def tinh_thuong(self):
        return self.get_luong() * 0.15 + self.so_nhan_vien * 200000

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print("So nhan vien quan ly:", self.so_nhan_vien)

nhan_vien1 = Employee("An", 8000000, "Ke toan")

nhan_vien2 = Developer(
    "Binh",
    12000000,
    "IT",
    "Python",
    10
)

nhan_vien3 = Developer(
    "Cuong",
    15000000,
    "IT",
    "Java",
    5
)

nhan_vien4 = Manager(
    "Dung",
    20000000,
    "Quan ly",
    8
)

danh_sach_nhan_vien = [
    nhan_vien1,
    nhan_vien2,
    nhan_vien3,
    nhan_vien4
]

print("THONG TIN NHAN VIEN")

for nhan_vien in danh_sach_nhan_vien:
    nhan_vien.hien_thi_thong_tin()


nhan_vien_luong_cao_nhat = danh_sach_nhan_vien[0]

for nhan_vien in danh_sach_nhan_vien:
    if nhan_vien.get_luong() > nhan_vien_luong_cao_nhat.get_luong():
        nhan_vien_luong_cao_nhat = nhan_vien

print("Nhan vien co luong cao nhat:")
print(nhan_vien_luong_cao_nhat.ten)
print(nhan_vien_luong_cao_nhat.get_luong())


tong_tien_thuong = 0

for nhan_vien in danh_sach_nhan_vien:
    tong_tien_thuong += nhan_vien.tinh_thuong()

print("Tong tien thuong:", tong_tien_thuong)


so_developer = 0
so_manager = 0

for nhan_vien in danh_sach_nhan_vien:
    if isinstance(nhan_vien, Developer):
        so_developer += 1

    if isinstance(nhan_vien, Manager):
        so_manager += 1

print("So Developer:", so_developer)
print("So Manager:", so_manager)

#BAI02 :
class Character:
    def __init__(self, ten, hp, level):
        self.ten = ten
        self.__hp = hp
        self._level = level

    def get_hp(self):
        return self.__hp

    def nhan_sat_thuong(self, sat_thuong):
        if sat_thuong > 0:
            self.__hp -= sat_thuong

            if self.__hp < 0:
                self.__hp = 0

    def hoi_mau(self, so_mau):
        if so_mau > 0:
            self.__hp += so_mau

    def tan_cong(self):
        return 0

    def hien_thi_thong_tin(self):
        print("Ten:", self.ten)
        print("HP:", self.get_hp())
        print("Level:", self._level)


class Warrior(Character):
    def __init__(self, ten, hp, level, suc_manh):
        super().__init__(ten, hp, level)
        self.suc_manh = suc_manh

    def tan_cong(self):
        sat_thuong = self._level * 5 + self.suc_manh
        return sat_thuong

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print("Suc manh:", self.suc_manh)


class Mage(Character):
    def __init__(self, ten, hp, level, mana, suc_manh_phep):
        super().__init__(ten, hp, level)
        self.__mana = mana
        self.suc_manh_phep = suc_manh_phep

    def get_mana(self):
        return self.__mana

    def tan_cong(self):
        if self.__mana < 10:
            return 0

        self.__mana -= 10

        sat_thuong = self._level * 3 + self.suc_manh_phep

        return sat_thuong

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print("Mana:", self.get_mana())
        print("Suc manh phep:", self.suc_manh_phep)


chien_binh1 = Warrior("Chien binh A", 150, 5, 20)

chien_binh2 = Warrior("Chien binh B", 180, 4, 25)

phap_su1 = Mage("Phap su A", 100, 6, 50, 30)

phap_su2 = Mage("Phap su B", 120, 5, 40, 35)


danh_sach_nhan_vat = [
    chien_binh1,
    chien_binh2,
    phap_su1,
    phap_su2
]


print("THONG TIN BAN DAU")

for nhan_vat in danh_sach_nhan_vat:
    nhan_vat.hien_thi_thong_tin()


sat_thuong = chien_binh1.tan_cong()
phap_su1.nhan_sat_thuong(sat_thuong)

print(
    chien_binh1.ten,
    "tan cong",
    phap_su1.ten,
    "gay",
    sat_thuong,
    "sat thuong"
)


sat_thuong = phap_su1.tan_cong()
chien_binh1.nhan_sat_thuong(sat_thuong)

print(
    phap_su1.ten,
    "tan cong",
    chien_binh1.ten,
    "gay",
    sat_thuong,
    "sat thuong"
)


sat_thuong = chien_binh2.tan_cong()
phap_su2.nhan_sat_thuong(sat_thuong)

print(
    chien_binh2.ten,
    "tan cong",
    phap_su2.ten,
    "gay",
    sat_thuong,
    "sat thuong"
)


sat_thuong = phap_su2.tan_cong()
chien_binh2.nhan_sat_thuong(sat_thuong)

print(
    phap_su2.ten,
    "tan cong",
    chien_binh2.ten,
    "gay",
    sat_thuong,
    "sat thuong"
)


print("\nTHONG TIN SAU KHI CHIEN DAU")

for nhan_vat in danh_sach_nhan_vat:
    nhan_vat.hien_thi_thong_tin()


nhan_vat_nhieu_hp_nhat = danh_sach_nhan_vat[0]

for nhan_vat in danh_sach_nhan_vat:
    if nhan_vat.get_hp() > nhan_vat_nhieu_hp_nhat.get_hp():
        nhan_vat_nhieu_hp_nhat = nhan_vat

print("Nhan vat con nhieu HP nhat:")
print(
    nhan_vat_nhieu_hp_nhat.ten,
    "- HP:",
    nhan_vat_nhieu_hp_nhat.get_hp()
)


print("\nKIEM TRA isinstance()")

print(
    "chien_binh1 co phai Warrior khong?",
    isinstance(chien_binh1, Warrior)
)

print(
    "phap_su1 co phai Mage khong?",
    isinstance(phap_su1, Mage)
)

print(
    "chien_binh1 co phai Character khong?",
    isinstance(chien_binh1, Character)
)


print("\nKIEM TRA issubclass()")

print(
    "Warrior co ke thua Character khong?",
    issubclass(Warrior, Character)
)

print(
    "Mage co ke thua Character khong?",
    issubclass(Mage, Character)
)

print(
    "Character co ke thua Warrior khong?",
    issubclass(Character, Warrior)
)