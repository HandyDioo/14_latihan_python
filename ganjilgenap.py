def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print(angka, "adalah bilangan GENAP")
    else:
        print(angka, "adalah bilangan GANJIL")

def cek_prima(angka):
    if angka < 2:
        print(angka, "bukan bilangan prima")
        return

    for i in range(2, angka):
        if angka % i == 0:
            print(angka, "bukan bilangan prima")
            return

    print(angka, "adalah bilangan prima")


while True:
    angka = int(input("Masukkan sebuah bilangan : "))

    cek_ganjil_genap(angka)
    cek_prima(angka)
    ulang = input("Apakah Anda ingin memasukkan bilangan lain? (Y/N): ")

    if ulang.upper() != "Y":
        print("Program selesai. Have a nice day!")
        break