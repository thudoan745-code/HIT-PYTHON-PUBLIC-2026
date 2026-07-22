#BAI01:
month = int(input("Nhap thang : "))
year = int(input("Nhap nam : "))
if month<1 or month>12 :
    print("Khong hop le!")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
    print("So ngay cua thang : ",31)
elif month==4 or month==6 or month==9 or month==11 :
    print("So ngay cua thang : ",30)
else :
    if year%400==0 or (year%4==0 and year%100!=0) :
        print("La nam nhuan, so ngay la : ",29)
    else :
        print("So ngay cua thang la : ",28)

#BAI02:
day = int(input("Nhap ngay sinh : "))
month = int(input("Nhap thang sinh : "))
year = int(input("Nhap nam sinh : "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
    max_day = 31
elif month==4 or month==6 or month==9 or month==11 :
    max_day = 30
elif month==2 :
    if year%400==0 or (year%4==0 and year%100!=0) :
        print("La nam nhuan!")
        max_day = 29
    else :
        max_day = 28
else :
    max_day = 0
#Kiem tra tinh hop le cua ngay, thang:
if month<1 or month>12 or day<1 or day>max_day :
    print("Ngay thang khong hop le!")
else :
    if (month==3 and day>=21) or (month==4 and day<=19) :
        print("Cung Bach Duong")
    elif (month==4 and day>=20) or (month==5 and day<=20) :
        print("Cung Kim Nguu")
    elif (month==5 and day>=21) or (month==6 and day<=20) :
        print("Cung Song Tu")
    elif(month==6 and day>=21) or (month==7 and day<=22) :
        print("Cung Cu Giai")
    elif(month==7 and day>=23) or (month==8 and day<=22) :
        print("Cung Su Tu")
    elif(month==8 and day>=23) or (month==9 and day<=22) :
        print("Cung Xu Nu")
    elif(month==9 and day>=23) or (month==10 and day<=22) :
        print("Cung Thien Binh")
    elif(month==10 and day>=23) or (month==11 and day<=21) :
        print("Cung Bo Cap")
    elif(month==11 and day>=22) or (month==12 and day<=21) :
        print("Cung Nhan Ma")
    elif(month==12 and day>=22) or (month==1 and day<=19) :
        print("Cung Ma Ket")
    elif(month==1 and day>=20) or (month==2 and day<=18) :
        print("Cung Bao Binh")
    else :
        print("Cung Song Ngu")

#BAI03 : Kiem tra so nguyen to
n = int(input("Nhap so nguyen n : "))
#Đếm
temp = abs(n)
count = 0
if temp == 0 :
    count = 1
else :
    while temp>0 :
        count += 1
        temp //= 10
#Tính tổng
temp = abs(n)
total = 0
while temp>0 :
    total += temp % 10
    temp //= 10
#Kiem tra so nguyen to(prime number)
if n<2 :
    prime_number = False
else :
    prime_number = True
    for i in range(2, n):
        if n % i == 0:
             prime_number = False
             break
        
print("So chu so : ",count)
print("Tong chu so :",total)
if prime_number :
    print("La so nguyen to !")
else : 
    print("Khong la so nguyen to !")

#BAI04:
N = int(input("Nhap so tien N : "))
so_bia_ban_dau = N//28
so_vo_bia = so_bia_ban_dau
tong_bia = so_bia_ban_dau
while so_vo_bia >=3 :
    new_bia = so_vo_bia // 3
    tong_bia += new_bia
    so_vo_bia = so_vo_bia % 3 + new_bia
print("So bia co the mua duoc la : ",tong_bia)
