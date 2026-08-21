import numpy as np

kills = np.random.randint(5, 31, 5)
deaths = np.random.randint(1, 16, 5)
assists = np.random.randint(1, 11, 5)
combat_score = np.random.randint(100, 351, 5)

bang = np.column_stack((kills, deaths, assists, combat_score))

print("Bang thong ke 5 tran (Kills - Deaths - Assists - Combat Score):")
print(bang)

print("---")

kda_3_tran = bang[-3:, :3]

print("Bang K-D-A cua 3 tran gan nhat:")
print(kda_3_tran)

print("---")

kd = np.round(bang[:, 0] / bang[:, 1], 2)

print("Chi so K/D tung tran:", kd)

print("---")

kills_cao_nhat = np.max(bang[:, 0])
tong_assists = np.sum(bang[:, 2])
combat_thap_nhat = np.min(bang[:, 3])

print("Kills ky luc:", kills_cao_nhat)
print("Tong Assists:", tong_assists)
print("Combat Score cham day:", combat_thap_nhat)

print("---")

bang_chuyen_doi = bang.T

print("Du lieu chuan bi ve bieu do (Transposed):")
print(bang_chuyen_doi)