while True:
    angka = int(input("Masukkan sebuah bilangan : "))

    if angka % 2 == 0:
        print(angka, "adalah bilangan GENAP")
    else:
        print(angka, "adalah bilangan GANJIL")

    ulang = input("Apakah Anda ingin memasukkan bilangan lain? (y/n): ")

    if ulang.lower() !="y":
        print("Program selesai. Have a nice day honeyyyyyyyyyyyyyy😘😘🥰🥰")
        break