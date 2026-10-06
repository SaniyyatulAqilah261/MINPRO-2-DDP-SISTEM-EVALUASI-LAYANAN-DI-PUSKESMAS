import os
from prettytable import PrettyTable
import pwinput

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "pasien": {"password": "user123", "role": "user"}
}

data_evaluasi = {
    1: {"nama": "Budi", "layanan": "Poli Umum", "nilai": 85},
    2: {"nama": "Siti", "layanan": "Poli Gigi", "nilai": 90},
    3: {"nama": "Rina", "layanan": "Poli KIA", "nilai": 88}
}

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_data():
    if not data_evaluasi:
        print("\nData evaluasi masih kosong.")
        return False
    table = PrettyTable()
    table.field_names = ["ID", "Nama Pasien", "Layanan Poli", "Nilai Evaluasi"]
    for key, val in data_evaluasi.items():
        table.add_row([key, val["nama"], val["layanan"], val["nilai"]])
    print("\n--- DATA EVALUASI LAYANAN PUSKESMAS ---")
    print(table)
    return True

def tambah_data():
    print("\n--- TAMBAH DATA EVALUASI BARU ---")
    nama_input = input("Masukkan nama pasien: ")
    if not nama_input.strip():
        print("[GAGAL] Nama pasien tidak boleh kosong!\n")
        return

    print("\nPilih Poli/Layanan:")
    print("1. Poli Umum")
    print("2. Poli Gigi")
    print("3. Poli KIA")
    pilihan_poli = input("Pilih poli (1-3): ")

    if pilihan_poli == "1":
        layanan_input = "Poli Umum"
    elif pilihan_poli == "2":
        layanan_input = "Poli Gigi"
    elif pilihan_poli == "3":
        layanan_input = "Poli KIA"
    else:
        print("[GAGAL] Pilihan poli tidak valid!\n")
        return

    try:
        nilai_angka = int(input("Masukkan nilai evaluasi (1-100): "))
        if 1 <= nilai_angka <= 100:
            new_id = max(data_evaluasi.keys(), default=0) + 1
            data_evaluasi[new_id] = {
                "nama": nama_input,
                "layanan": layanan_input,
                "nilai": nilai_angka
            }
            print("[BERHASIL] Data evaluasi berhasil disimpan!\n")
        else:
            print("[GAGAL] Nilai harus berada dalam rentang 1 - 100!\n")
    except ValueError:
        print("[GAGAL] Input nilai harus berupa angka bulat!\n")

def ubah_data():
    print("\n--- UBAH DATA EVALUASI ---")
    if not tampilkan_data():
        return
    try:
        id_ubah = int(input("\nMasukkan ID data yang ingin diubah: "))
        if id_ubah in data_evaluasi:
            nama_baru = input(f"Masukkan nama baru ({data_evaluasi[id_ubah]['nama']}): ")
            if not nama_baru.strip():
                nama_baru = data_evaluasi[id_ubah]['nama']

            print("\nPilih Poli/Layanan Baru:")
            print("1. Poli Umum")
            print("2. Poli Gigi")
            print("3. Poli KIA")
            print("4. Tidak Mengubah Poli")
            pilihan_poli = input("Pilih poli (1-4): ")

            if pilihan_poli == "1":
                layanan_baru = "Poli Umum"
            elif pilihan_poli == "2":
                layanan_baru = "Poli Gigi"
            elif pilihan_poli == "3":
                layanan_baru = "Poli KIA"
            elif pilihan_poli == "4":
                layanan_baru = data_evaluasi[id_ubah]['layanan']
            else:
                print("[GAGAL] Pilihan poli tidak valid!\n")
                return

            input_nilai = input(f"Masukkan nilai baru (1-100) ({data_evaluasi[id_ubah]['nilai']}): ")
            if input_nilai.strip() == "":
                nilai_baru = data_evaluasi[id_ubah]['nilai']
            else:
                nilai_baru = int(input_nilai)
                if not (1 <= nilai_baru <= 100):
                    print("[GAGAL] Nilai harus berada dalam rentang 1 - 100!\n")
                    return

            data_evaluasi[id_ubah] = {
                "nama": nama_baru,
                "layanan": layanan_baru,
                "nilai": nilai_baru
            }
            print("[BERHASIL] Data evaluasi berhasil diperbarui!\n")
        else:
            print("[GAGAL] ID data tidak ditemukan!\n")
    except ValueError:
        print("[GAGAL] Input ID atau nilai harus berupa angka!\n")

def hapus_data():
    print("\n--- HAPUS DATA EVALUASI ---")
    if not tampilkan_data():
        return
    try:
        id_hapus = int(input("\nMasukkan ID data yang ingin dihapus: "))
        if id_hapus in data_evaluasi:
            del data_evaluasi[id_hapus]
            print("[BERHASIL] Data evaluasi berhasil dihapus!\n")
        else:
            print("[GAGAL] ID data tidak ditemukan!\n")
    except ValueError:
        print("[GAGAL] Input ID harus berupa angka!\n")

def login():
    bersihkan_layar()
    print("\n--------------------------------------")
    print("SISTEM EVALUASI LAYANAN PUSKESMAS")
    print("--------------------------------------")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if username in users and users[username]["password"] == password:
        return username, users[username]["role"]
    else:
        print("[GAGAL] Username atau password salah!\n")
        return None, None

def menu_admin():
    bersihkan_layar()
    while True:
        print("\n--------------------------------------")
        print("MENU ADMIN - SISTEM EVALUASI PUSKESMAS")
        print("--------------------------------------")
        print("1. Tampilkan Seluruh Data")
        print("2. Tambah Data Baru")
        print("3. Ubah Data Evaluasi")
        print("4. Hapus Data Evaluasi")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            bersihkan_layar()
            tampilkan_data()
        elif pilihan == "2":
            bersihkan_layar()
            tambah_data()
        elif pilihan == "3":
            bersihkan_layar()
            ubah_data()
        elif pilihan == "4":
            bersihkan_layar()
            hapus_data()
        elif pilihan == "5":
            bersihkan_layar()
            print("\n[INFO] Berhasil logout dari akun Admin.")
            break
        else:
            print("[ERROR] Pilihan menu tidak valid!")

def menu_user():
    bersihkan_layar()
    while True:
        print("\n--------------------------------------")
        print("MENU USER - SISTEM EVALUASI PUSKESMAS")
        print("--------------------------------------")
        print("1. Tampilkan Seluruh Data")
        print("2. Tambah Data Evaluasi")
        print("3. Logout")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            bersihkan_layar()
            tampilkan_data()
        elif pilihan == "2":
            bersihkan_layar()
            tambah_data()
        elif pilihan == "3":
            bersihkan_layar()
            print("\n[INFO] Berhasil logout dari akun User.")
            break
        else:
            print("[ERROR] Pilihan menu tidak valid!")

def main():
    bersihkan_layar()
    while True:
        print("\n--------------------------------------")
        print("SELAMAT DATANG DI PUSKESMAS EVALUATION")
        print("--------------------------------------")
        print("1. Login")
        print("2. Keluar Program")
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            username, role = login()
            if role == "admin":
                bersihkan_layar()
                print(f"\n[SUCCESS] Login Berhasil sebagai Admin ({username})!")
                menu_admin()
            elif role == "user":
                bersihkan_layar()
                print(f"\n[SUCCESS] Login Berhasil sebagai User ({username})!")
                menu_user()
        elif pilihan == "2":
            bersihkan_layar()
            print("\nProgram selesai. Terima kasih telah menggunakan layanan ini!")
            break
        else:
            print("[ERROR] Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()
