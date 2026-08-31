import modulmatematika
import modulolahkata

def main():
    while True:
        print("\n======= MENU PROGRAM =======")
        print("1. Program Bilangan Ganjil Genap")
        print("2. Program Bilangan Prima")
        print("3. Program Menyapa Nama")
        print("4. Keluar")
        
        pilihan = input("Pilih Menu (1-4): ")

        if pilihan == "1":
            angka = int(input("Masukkan Angka: "))
            modulmatematika.cek_ganjil_genap(angka)

        elif pilihan == "2":
            angka = int(input("Masukkan Angka: "))
            modulmatematika.cek_prima(angka)

        elif pilihan == "3":
            nama = input("Masukkan Nama: ")
            modulolahkata.sapa_dan_kapital(nama)

        elif pilihan == "4":
            print("======= Terima kasih! Program selesai. Have a nice day! =======")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
