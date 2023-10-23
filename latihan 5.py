# Fungsi penambahan
from decimal import DivisionImpossible
from signal import default_int_handler


def tambah(angka1, angka2):
    return angka1 + angka2

# Fungsi pengurangan
def kurang(angka1, angka2):
    return angka1 - angka2

# Fungsi perkalian
def kali(angka1, angka2):
    return angka1 * angka2

# Fungsi pembagian
def bagi(angka1, angka2):
    if angka2 == 0:
        return "Tidak dapat dibagi oleh nol"
    return angka1 / angka2

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Pilih operasi:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Keluar")

# Loop utama
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan : ")

    if pilihan == '0':
        print("Program Selesai.")
        break

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            hasil = tambah(angka1, angka2)
            operasi = "Penambahan"
        elif pilihan == '2':
            hasil = kurang(angka1, angka2)
            operasi = "Pengurangan"
        elif pilihan == '3':
            hasil = kali(angka1, angka2)
            operasi = "Perkalian"
        else:
            hasil = bagi(angka1, angka2)
            operasi = "Pembagian"

        print(f"Hasil {operasi}: {hasil}\n")
    else:
        print("Pilihan tidak valid. Silakan pilih operasi yang benar.\n")