class Weapon:

    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def reload(self, so_dan=None):
        if so_dan is not None:
            self.ammo += so_dan
            print(self.name + " nap " + str(so_dan) + " vien -> Dan:", self.ammo)
        else:
            self.ammo = 30
            print(self.name + " nap day -> Dan:", self.ammo)


class Vandal(Weapon):

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print("[Vandal] Dung! - Dan con:", self.ammo)
        else:
            print("[Vandal] Het dan!")


class Operator(Weapon):

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print("[Operator] DOANG! - Dan con:", self.ammo)
        else:
            print("[Operator] Het dan!")


class JettSkill:

    def __init__(self, dao):
        self.dao = dao

    def shoot(self):
        if self.dao > 0:
            self.dao -= 1
            print("[JettSkill] Phong dao! - Dao con:", self.dao)
        else:
            print("[JettSkill] Het dao!")


def perform_attack(entity, times):
    for i in range(times):
        entity.shoot()


vandal = Vandal("Vandal", 30)
operator = Operator("Operator", 5)
jett = JettSkill(5)

danh_sach = [vandal, operator, jett]

for doi_tuong in danh_sach:
    perform_attack(doi_tuong, 2)

print("---")

vandal.reload(10)
vandal.reload()