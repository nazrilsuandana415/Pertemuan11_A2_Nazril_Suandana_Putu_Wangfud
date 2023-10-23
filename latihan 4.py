def hitung_jumlah_angka_dapat_dibagi(daftar_angka, pemisah):
    jumlah = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            jumlah += angka
    return jumlah

# Contoh penggunaan fungsi dengan list angka dan angka pemisah yang berbeda
angka_1 = [12,14,15,18,20]
pemisah_1 = 2
hasil_1 = hitung_jumlah_angka_dapat_dibagi(angka_1, pemisah_1)
print(f"Jumlah angka dalam daftar yang dapat dibagi habis oleh {pemisah_1} adalah {hasil_1}")

angka_2 = [5, 15, 25, 35, 45]
pemisah_2 = 5
hasil_2 = hitung_jumlah_angka_dapat_dibagi(angka_2, pemisah_2)
print(f"Jumlah angka dalam daftar yang dapat dibagi habis oleh {pemisah_2} adalah {hasil_2}")
