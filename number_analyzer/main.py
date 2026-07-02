n=int(input())
while n<=0:
    print(f"Vui long nhap n>0 ")
    n=int(input())
tong=0
sochan=0
sole=0

if n%2==0:
    print(f"{n} la so chan")
else:
    print(f"{n} la so le")


if n%3==0:
    print(f"{n} chia het cho 3")
else:
    print(f"{n} khong chia het cho 3")
if n%5==0:
    print(f"{n} chia het cho 5")
else:
    print(f"{n} khong chia het cho 5")


for i in range(1,n+1,1):
    tong+=i
print(f"Tong cac so tu 1 den {n} = {tong}")


for i in range(1,n+1,1):
    if i%2==0:
        sochan+=1
    else:
        sole+=1
print(f"So luong so chan tu 1 den {n} = {sochan}")
print(f"So luong so le tu 1 den {n} = {sole}")