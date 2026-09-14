import tkinter as tk
from tkinter import messagebox
import mysql.connector, modulmatematika, modulolahkata

PASSWORD_MYSQL = "rahasiaadmin123"

def buat_koneksi():
    return mysql.connector.connect(host="localhost", user="root", password=PASSWORD_MYSQL, database="login_db")

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Modul GUI")
        self.root.geometry("450x600")
        self.root.configure(bg="#F8FAFC")
        self.root.resizable(False, False)
        self.user_aktif = ""
        self.halaman_awal()

    def buat_card(self, height=480):
        for w in self.root.winfo_children(): w.destroy()
        card = tk.Frame(self.root, bg="#FFFFFF", bd=0, highlightthickness=1, highlightbackground="#E2E8F0")
        card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=height)
        return card

    def buat_btn(self, parent, text, bg, cmd, pady=6, ipady=8):
        btn = tk.Button(parent, text=text, font=("Helvetica", 10, "bold"), bg=bg, fg="white", bd=0, cursor="hand2", command=cmd)
        btn.pack(fill="x", padx=35, pady=pady, ipady=ipady)
        return btn

    def buat_entry(self, parent, label_text, is_pass=False):
        tk.Label(parent, text=label_text, font=("Helvetica", 8, "bold"), bg="#FFFFFF", fg="#475569").pack(anchor="w", padx=35)
        entry = tk.Entry(parent, font=("Helvetica", 11), bg="#F8FAFC", fg="#0F172A", bd=1, relief="solid", show="•" if is_pass else "")
        entry.pack(fill="x", padx=35, pady=(5, 15), ipady=7)
        return entry

    # 1. HALAMAN AWAL
    def halaman_awal(self):
        card = self.buat_card(450)
        tk.Label(card, text="SELAMAT DATANG", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#0F172A").pack(pady=(40, 5))
        tk.Label(card, text="Aplikasi Sistem Modul & Autentikasi", font=("Helvetica", 10), bg="#FFFFFF", fg="#64748B").pack(pady=(0, 35))
        self.buat_btn(card, "LOGIN", "#3B82F6", self.halaman_login, 8, 10)
        self.buat_btn(card, "REGISTER", "#10B981", self.halaman_register, 8, 10)
        self.buat_btn(card, "EXIT / KELUAR", "#EF4444", self.root.quit, 8, 10)

    # 2. HALAMAN LOGIN
    def halaman_login(self):
        card = self.buat_card()
        tk.Label(card, text="Menu Login", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#0F172A").pack(pady=(30, 5))
        tk.Label(card, text="Masukkan kredensial akun Anda", font=("Helvetica", 9), bg="#FFFFFF", fg="#64748B").pack(pady=(0, 25))
        self.ent_user = self.buat_entry(card, "USERNAME")
        self.ent_pass = self.buat_entry(card, "PASSWORD", True)
        self.buat_btn(card, "MASUK", "#3B82F6", self.proses_login, (5, 10))
        tk.Button(card, text="← Kembali ke Menu Awal", font=("Helvetica", 9), bg="#FFFFFF", fg="#64748B", bd=0, cursor="hand2", command=self.halaman_awal).pack(pady=5)

    def proses_login(self):
        u, p = self.ent_user.get().strip(), self.ent_pass.get().strip()
        if not u or not p: return messagebox.showwarning("Peringatan", "Username dan Password harus diisi!")
        try:
            conn = buat_koneksi()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (u, p))
            if cursor.fetchone():
                self.user_aktif = u
                messagebox.showinfo("Berhasil", f"Selamat datang, {u}!")
                self.halaman_pilih_program()
            else: messagebox.showerror("Gagal Login", "Username atau Password salah!")
            cursor.close(); conn.close()
        except mysql.connector.Error as err: messagebox.showerror("Database Error", f"Kesalahan koneksi:\n{err}")

    # 3. HALAMAN REGISTER
    def halaman_register(self):
        card = self.buat_card()
        tk.Label(card, text="Registrasi Akun", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#0F172A").pack(pady=(30, 5))
        tk.Label(card, text="Buat username dan password baru", font=("Helvetica", 9), bg="#FFFFFF", fg="#64748B").pack(pady=(0, 25))
        self.ent_reg_user = self.buat_entry(card, "USERNAME BARU")
        self.ent_reg_pass = self.buat_entry(card, "PASSWORD BARU", True)
        self.buat_btn(card, "DAFTAR SEKARANG", "#10B981", self.proses_register, (5, 10))
        tk.Button(card, text="← Kembali ke Menu Awal", font=("Helvetica", 9), bg="#FFFFFF", fg="#64748B", bd=0, cursor="hand2", command=self.halaman_awal).pack(pady=5)

    def proses_register(self):
        u, p = self.ent_reg_user.get().strip(), self.ent_reg_pass.get().strip()
        if not u or not p: return messagebox.showwarning("Peringatan", "Harap isi semua bidang!")
        try:
            conn = buat_koneksi()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (u, p))
            conn.commit()
            messagebox.showinfo("Berhasil", f"Akun '{u}' berhasil dibuat! Silakan login.")
            cursor.close(); conn.close()
            self.halaman_login()
        except mysql.connector.Error as err:
            msg = "Username sudah terpakai!" if err.errno == 1062 else f"Kesalahan:\n{err}"
            messagebox.showerror("Gagal", msg)

    # 4. SUB-MENU
    def halaman_pilih_program(self):
        card = self.buat_card()
        tk.Label(card, text=f"Halo, {self.user_aktif}! 👋", font=("Helvetica", 16, "bold"), bg="#FFFFFF", fg="#0F172A").pack(pady=(25, 5))
        tk.Label(card, text="Pilih program yang ingin dijalankan:", font=("Helvetica", 9), bg="#FFFFFF", fg="#64748B").pack(pady=(0, 20))
        self.buat_btn(card, "1. Program Ganjil / Genap", "#4F46E5", lambda: self.halaman_eksekusi_program("ganjil_genap"))
        self.buat_btn(card, "2. Program Bilangan Prima", "#8B5CF6", lambda: self.halaman_eksekusi_program("prima"))
        self.buat_btn(card, "3. Program Sapa Nama", "#EC4899", lambda: self.halaman_eksekusi_program("sapa"))
        self.buat_btn(card, "Logout", "#EF4444", self.halaman_awal, (20, 0), 6)

    # 5. HALAMAN EKSEKUSI PROGRAM
    def halaman_eksekusi_program(self, jenis_program):
        card = self.buat_card()
        info = {
            "ganjil_genap": ("Cek Ganjil / Genap", "MASUKKAN ANGKA:"),
            "prima": ("Cek Bilangan Prima", "MASUKKAN ANGKA:"),
            "sapa": ("Menyapa Nama", "MASUKKAN NAMA:")
        }
        judul, label_input = info[jenis_program]

        tk.Label(card, text=judul, font=("Helvetica", 16, "bold"), bg="#FFFFFF", fg="#0F172A").pack(pady=(25, 15))
        self.ent_program_input = self.buat_entry(card, label_input)
        self.buat_btn(card, "PROSES DATA", "#0EA5E9", lambda: self.proses_eksekusi(jenis_program), 5)

        tk.Label(card, text="HASIL OUTPUT:", font=("Helvetica", 8, "bold"), bg="#FFFFFF", fg="#475569").pack(anchor="w", padx=35, pady=(15, 5))
        self.box_hasil = tk.Frame(card, bg="#F1F5F9", bd=1, relief="solid")
        self.box_hasil.pack(fill="x", padx=35, pady=(0, 15), ipady=12)
        self.lbl_hasil = tk.Label(self.box_hasil, text="[ Hasil akan muncul di sini ]", font=("Helvetica", 9, "italic"), bg="#F1F5F9", fg="#64748B", wraplength=280)
        self.lbl_hasil.pack(padx=10, pady=5)
        tk.Button(card, text="← Kembali ke Pilih Program", font=("Helvetica", 9), bg="#FFFFFF", fg="#64748B", bd=0, cursor="hand2", command=self.halaman_pilih_program).pack(pady=5)

    def proses_eksekusi(self, jenis_program):
        val = self.ent_program_input.get().strip()
        if jenis_program in ["ganjil_genap", "prima"]:
            if val.isdigit():
                hasil = modulmatematika.cek_ganjil_genap(int(val)) if jenis_program == "ganjil_genap" else modulmatematika.cek_prima(int(val))
                self.lbl_hasil.config(text=hasil, font=("Helvetica", 10, "bold"), fg="#047857")
                self.box_hasil.config(bg="#D1FAE5")
            else:
                self.lbl_hasil.config(text="❌ Masukkan angka bulat yang valid!", font=("Helvetica", 9, "bold"), fg="#DC2626")
                self.box_hasil.config(bg="#FEE2E2")
        elif jenis_program == "sapa":
            if val:
                self.lbl_hasil.config(text=modulolahkata.sapa_dan_kapital(val), font=("Helvetica", 10, "bold"), fg="#047857")
                self.box_hasil.config(bg="#D1FAE5")
            else:
                self.lbl_hasil.config(text="❌ Input nama tidak boleh kosong!", font=("Helvetica", 9, "bold"), fg="#DC2626")
                self.box_hasil.config(bg="#FEE2E2")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernApp(root)
    root.mainloop()
