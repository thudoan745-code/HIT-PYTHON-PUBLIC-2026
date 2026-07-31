def tim_tu(chuoi, target):
    words = chuoi.split()
    found = False
    for i in range(len(words)):
        if words[i] == target:
            print(i)
            found = True
    if found == False:
        print(-1)
chuoi = input("Nhap chuoi: ")
target = input("Nhap tu can tim: ")
tim_tu(chuoi, target)