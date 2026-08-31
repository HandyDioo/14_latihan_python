#Fungsi Bilangan Ganjil Genap
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print(angka, "adalah bilangan GENAP")
    else:
        print(angka, "adalah bilangan GANJIL")

#Fungsi Bilangan Prima
def cek_prima(angka):
    if angka < 2:
        print(angka, "BUKAN bilangan prima")
        return

    for i in range(2, angka):
        if angka % i == 0:
            print(angka, "BUKAN bilangan prima")
            return
        
    print(angka, "ADALAH bilangan prima")
