def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print(angka, "adalah bilangan GENAP")
    else:
        print(angka, "adalah bilangan GANJIL")

def cek_prima(angka):
    if angka < 2:
        print(angka, "BUKAN bilangan prima")
        return

    for i in range(2, angka):
        if angka % i == 0:
            print(angka, "BUKAN bilangan prima")
            return
        
    print(angka, "ADALAH bilangan prima")

while True:
    print("\n=== MENU PROGRAM PYTHON ===")
    print("1. Program Ganjil Genap")
    print("2. Program Bilangan Prima")
    print("3. Exit")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":

        while True:
            angka = int(input("Masukkan sebuah bilangan: "))
            cek_ganjil_genap(angka)

            ulang = input("Ingin memasukkan bilangan lagi? (Y/N): ")

            if ulang.upper() != "Y":
                break

    elif pilihan == "2":

        while True:
            angka = int(input("Masukkan sebuah bilangan: "))
            cek_prima(angka)

            ulang = input("Ingin memasukkan bilangan prima lagi? (Y/N): ")

            if ulang.upper() != "Y":
                break

    elif pilihan == "3":
        print("Keluar program...")
        print("Program selesai. Have a nice day!")
        break

    else:
        print("Pilihan tidak valid.")