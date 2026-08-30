def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print(angka, "adalah bilangan GENAP")
    else:
        print(angka, "adalah bilangan GANJIL")


while True:
    angka = int(input("Masukkan sebuah bilangan : "))

    cek_ganjil_genap(angka)

    ulang = input("Apakah Anda ingin memasukkan bilangan lain? (Y/N): ")

    if ulang.upper() != "Y":
        print("Program selesai.")
        break