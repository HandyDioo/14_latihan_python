import mysql.connector
import modulmatematika
import modulolahkata

PASSWORD_MYSQL = "rahasiaadmin123" 

def buat_koneksi():
    """Fungsi untuk menghubungkan Python ke database MySQL"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=PASSWORD_MYSQL,
        database="login_db"
    )

def registrasi_user():
    """Fitur untuk membuat username dan password baru"""
    print("\n=== REGISTER NEW USER ===")
    print("(Ketik 'batal' atau 'kembali' untuk membatalkan)")

    username = input("Masukkan Username baru : ")

    # Opsi Pembatalan
    if username.lower() in ['batal', 'kembali']:
        print("↩️ Pendaftaran dibatalkan. Kembali ke gerbang aplikasi.")
        return # Langsung keluar dari fungsi registrasi_user

    password = input("Masukkan Password baru : ")

    conn = None
    cursor = None
    try:
        conn = buat_koneksi()
        cursor = conn.cursor()
        
        # Query SQL untuk memasukkan data user baru
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        
        conn.commit() # Menyimpan perubahan ke database
        print(f"🎉 Akun '{username}' berhasil didaftarkan!")
        
    except mysql.connector.Error as err:
        if err.errno == 1062: # Kode error jika username kembar atau sama
            print("❌ Gagal! Username sudah digunakan orang lain.")
        else:
            print(f"❌ Terjadi kesalahan: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def login_user():
    """Fungsi login untuk memeriksa kesesuaian username & password"""
    print("\n===== MENU LOGIN =====")
    print("(Ketik 'batal' atau 'kembali' untuk membatalkan)")

    username = input("Username : ")

    # Opsi Pembatalan
    if username.lower() in ['batal', 'kembali']:
        print("↩️ Login dibatalkan. Kembali ke gerbang aplikasi.")
        return False # Mengembalikan False agar program utama tidak terbuka

    password = input("Password : ")

    conn = None
    cursor = None
    try:
        conn = buat_koneksi()
        cursor = conn.cursor()
        
        # Mencari user dengan username dan password-nya cocok
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        
        user = cursor.fetchone() 
        
        if user:
            print(f"\n🔓 HORE! Selamat datang '{username}', anda berhasil masuk ke program!")
            return True
        else:
            print("\n❌ Login Gagal! Username atau password salah.")
            return False
            
    except mysql.connector.Error as err:
        print(f"❌ Terjadi kesalahan: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def menu_program_utama():
    """Menu program matematika dan olah kata milik Anda"""
    while True:
        print("\n======= MENU PROGRAM =======")
        print("1. Program Bilangan Ganjil Genap")
        print("2. Program Bilangan Prima")
        print("3. Program Menyapa Nama")
        print("4. Keluar dari Menu Program")
        
        pilihan = input("Pilih Menu (1-4): ")

        if pilihan == "1":
            angka = int(input("Masukkan Angka : "))
            modulmatematika.cek_ganjil_genap(angka)

        elif pilihan == "2":
            angka = int(input("Masukkan Angka : "))
            modulmatematika.cek_prima(angka)

        elif pilihan == "3":
            nama = input("Masukkan Nama : ")
            modulolahkata.sapa_dan_kapital(nama)

        elif pilihan == "4":
            print("======= Program selesai. Terima kasih! Have a nice day! =======")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# MENU UTAMA UNTUK LOGIN DAN REGISTRASI
def main():
    while True:
        print("\n===== AUTHENTICATION MENU =====")
        print("1. Register (Buat Akun Baru)")
        print("2. Login (Masuk Dengan Akun)")
        print("3. Keluar dari Menu Utama")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            registrasi_user()
        elif pilihan == '2':
            # Jika fungsi login bernilai True, maka gerbang utama akan terbuka
            if login_user():
                menu_program_utama() 
        elif pilihan == '3':
            print("Anda telah keluar dari menu utama.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
