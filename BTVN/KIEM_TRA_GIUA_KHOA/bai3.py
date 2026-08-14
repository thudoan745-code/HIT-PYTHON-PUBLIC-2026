def tim_tu(chuoi, tu_can_tim):
    words = chuoi.split()
    found = False
    for i in range(len(words)):
        if words[i] == tu_can_tim:
            print(i)
            found = True
    if found == False:
        print(-1)
chuoi = input("Nhap chuoi: ")
tu_can_tim = input("Nhap tu can tim: ")
tim_tu(chuoi, tu_can_tim)