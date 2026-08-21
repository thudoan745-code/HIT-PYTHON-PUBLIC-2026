from abc import ABC, abstractmethod

class HomeAppliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def operate(self):
        pass


class KitchenAppliance(HomeAppliance):

    def turn_on(self):
        print("Da cam dien va bat cong tac")

    @abstractmethod
    def operate(self):
        pass


class RiceCooker(KitchenAppliance):

    def operate(self):
        print("[RiceCooker] Hoat dong: Dang nau chin gao...")


class Microwave(KitchenAppliance):

    def operate(self):
        print("[Microwave] Hoat dong: Dang ham nong thuc an...")


try:
    bep = KitchenAppliance()
except TypeError:
    print("Loi: Khong the khoi tao KitchenAppliance vi thieu trien khai phuong thuc truu tuong 'operate'.")

print("---")

danh_sach = [RiceCooker(), Microwave()]

for thiet_bi in danh_sach:
    print("[" + thiet_bi.__class__.__name__ + "] ", end="")
    thiet_bi.turn_on()
    thiet_bi.operate()