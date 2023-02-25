print("Hesap makinesine hosgeldiniz")

firstnumber = int(input("Lutfen bir sayi giriniz: "))
secondnumber = int(input("Lutfen baska bir sayi daha giriniz: "))

print("Toplama islemi icin +")
print("Cikartma islemi icin -")
print("Carpma islemi icin *")
print("Bolme islemi icin /")

islem = input("Yapmak istediginiz islem icin isaret giriniz: ")

if(islem == "+"):
    print(firstnumber + secondnumber)
elif(islem == "-"):
    print(firstnumber - secondnumber)
if(islem == "*"):
    print(firstnumber * secondnumber)
elif(islem == "/"):
    print(firstnumber / secondnumber)