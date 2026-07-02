n=int(input("Nhap so luong hoc sinh = "))
while n<=0:
    n=int(input("Vui long nhap lai so luong hoc sinh = "))

scores=[]
names=[]

for i in range(n):
    ten=input(f"Ten hoc sinh thu {i+1} la : ")
    names.append(ten)
    x=float(input(f"Nhap diem hoc sinh thu {i+1} = "))
    while x<0 or x>10:
        x=float(input(f"Vui long nhap lai diem hoc sinh thu {i+1} = "))
    scores.append(x)

print(f"Danh sach ten = {names}")
print(f"Danh sach diem = {scores}")

tongdiem=0
for x in scores:
    tongdiem+=x
print(f"Diem trung binh = {tongdiem/n}")

max_value=scores[0]
max_location=0
min_value=scores[0]
min_location=0
for i in range(n):
    if scores[i]>max_value:
        max_value=scores[i]
    if scores[i]<min_value:
        min_value=scores[i]

print(f"Diem cao nhat la {max_value}\nHoc sinh co diem cao nhat:")
for i in range(n):
    if scores[i]==max_value:
        print(f"-{names[i]}")

print(f"Diem thap nhat la {min_value}\nHoc sinh co diem thap nhat:")
for i in range(n):
    if scores[i]==min_value:
        print(f"-{names[i]}")


count_gioi=0
count_kha=0
count_tb=0
count_yeu=0
count_qua=0
count_rot=0

for x in scores:
    if x>=8:
        count_gioi+=1
    elif x>=6.5:
        count_kha+=1
    elif x>=5:
        count_tb+=1
    else:
        count_yeu+=1

    if x>=5:
        count_qua+=1
    else:
        count_rot+=1

print(f"\nSo hoc sinh gioi la {count_gioi}\nSo hoc sinh kha la {count_kha}\nSo hoc sinh trung binh la {count_tb}\nSo hoc sinh yeu la {count_yeu}\n")
print(f"\nSo hoc sinh qua mon la {count_qua}\nSo hoc sinh rot mon la {count_rot}\n")