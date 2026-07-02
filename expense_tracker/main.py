n=int(input("Nhap so luong khoan chi = "))
while n<=0:
    n=int(input("So khoan chi ko phu hop, vui long nhap lai = "))

names=[]
amounts=[]
categories=[]

for i in range(n):
    x=input(f"Nhap ten khoan chi {i+1}: ")
    names.append(x)
    x=float(input(f"Nhap so tien: "))
    while x<=0:
        x=float(input(f"Vui long nhap lai so tien "))
    amounts.append(x)
    x=input("Nhap loai chi tieu: ")
    while x!='food' and x!='drink' and x!='transport' and x!='other':
        x=input("Loai chi tieu khong phu hop, vui long nhap lai ")
    categories.append(x)
    

for i in range(n):
    print(f"{names[i]} - {amounts[i]} - {categories[i]}")

tongchitieu=0
tongchitieufood=0
count_food=0
tongchitieudrink=0
count_drink=0
tongchitieutransport=0
count_transport=0
tongchitieuother=0
count_other=0
for x in amounts:
    tongchitieu+=x
print(f"Tong chi tieu la {tongchitieu}")
for i in range(n):
    if categories[i]=='food':
        tongchitieufood+=amounts[i]
        count_food+=1
    if categories[i]=='drink':
        count_drink+=1
        tongchitieudrink+=amounts[i]
    if categories[i]=='transport':
        count_transport+=1
        tongchitieutransport+=amounts[i]
    if categories[i]=='other':
        count_other+=1
        tongchitieuother+=amounts[i]
print(f"So khoan food: {count_food}")
print(f"So khoan drink: {count_drink}")
print(f"So khoan transport: {count_transport}")
print(f"So khoan other: {count_other}")
print(f"Tong chi tieu tung loai la: \n -food: {tongchitieufood}\n -drink: {tongchitieudrink}\n -transport: {tongchitieutransport}\n -other: {tongchitieuother}")
print(f"Chi tieu trung binh la {tongchitieu/n}")


max_amounts=amounts[0]
min_amounts=amounts[0]
for i in range(n):
    if amounts[i]>max_amounts:
        max_amounts=amounts[i]
    if amounts[i]<min_amounts:
        min_amounts=amounts[i]

print(f"Khoan chi tieu lon nhat la {max_amounts}")
print(f"Ten khoan chi la: ")
for i in range(n):
    if max_amounts==amounts[i]:
        print(f"- {names[i]}")

print(f"Khoan chi tieu nho nhat la {min_amounts}")
print(f"Ten khoan chi la: ")
for i in range(n):
    if min_amounts==amounts[i]:
        print(f"- {names[i]}")


count_over_100k=0
count_below_or_equal_100k=0
for x in amounts:
    if x>100000:
        count_over_100k+=1
    else:
        count_below_or_equal_100k+=1
print(f"\nSo khoan chi lon hon 100000 la {count_over_100k}\nSo khoan chi nho hon hoac bang 100000 la {count_below_or_equal_100k}")
