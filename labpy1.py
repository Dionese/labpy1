print("Program menentukan bilangan terbesar dari 3 bilangan")
a= int(input("masukan nilai ke-1= "))
b= int(input("masukan nilai ke-2= "))
c= int(input("masukan nilai ke-3= "))

print("Dari bilangan ",a,b,c)

if a > b and a > c:
    print(a, "adalah niai terbesar")
elif b > a and b > c:
    print(b, "adalah niai terbesar")
else:
    print(c, "adalah nilai terbesar")