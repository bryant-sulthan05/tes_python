import os

# Data awal
nama = ['Bryant Sulthan Nugroho', 'Muhammad Yusuf Ghazali', 'Raihanadri Putra Sarel', 'Farrel Amri Bustomi']
npm = ['50423286', '51423033', '51423212', '50423464']
keterangan = ['']*len(nama)

def absen(keterangan):
    for i in range(len(nama)):
        print(f"\nNama: {nama[i]}\nNPM: {npm[i]}")
        keterangan_input = input("Masukkan keterangan: ")
        keterangan[i] = keterangan_input
    return

def cari_dan_tampilkan_data(query):
    for i in range(len(nama)):
        kata_kata_nama = nama[i].lower().split()
        if query.lower() in kata_kata_nama or query.lower() in npm[i].lower():
            print(f"Nama: {nama[i]} \nNPM: {npm[i]}")
            print(f"Keterangan: {keterangan[i]}")
            keterangan_input = input("Masukkan keterangan baru: ")
            keterangan[i] = keterangan_input
            return
    print("Nama tidak ditemukan")

def tampilkan_data_berdasarkan_keterangan(ket):
    jumlah_nama = 0
    for i in range(len(nama)):
        if ket.lower() in keterangan[i].lower():
            print(f"\nNama: {nama[i]} \nNPM: {npm[i]} \nKeterangan: {keterangan[i]}")
            jumlah_nama += 1
    return jumlah_nama

# Fungsi untuk menampilkan semua data
def tampilkan_semua_data():
    jumlah_hadir = 0
    jumlah_sakit = 0
    jumlah_izin = 0
    jumlah_alpa = 0
    for i in range(len(nama)):
        if i < len(keterangan):
            print(f"\nNama: {nama[i]} \nNPM: {npm[i]} \nKeterangan: {keterangan[i]}")
            
            if 'hadir' in keterangan[i].lower():
                jumlah_hadir += 1
            elif 'sakit' in keterangan[i].lower():
                jumlah_sakit += 1
            elif 'izin' in keterangan[i].lower():
                jumlah_izin += 1
            elif 'tanpa keterangan' in keterangan[i].lower():
                jumlah_alpa += 1

    print("\nJumlah mahasiswa yang hadir:", jumlah_hadir)
    print("Jumlah mahasiswa yang sakit:", jumlah_sakit)
    print("Jumlah mahasiswa yang izin:", jumlah_izin)
    print("Jumlah mahasiswa yang tanpa keterangan:", jumlah_alpa)

while True:
    opsi = input("\nMasukkan opsi (absen/cari/daftar absen/selesai): ").lower()

    if opsi == 'selesai':
        break
    elif opsi == 'cari':
        query = input("Masukkan nama atau npm yang ingin dicari: ")
        cari_dan_tampilkan_data(query)
    elif opsi == 'daftar absen':
        tampilkan_semua_data()
    elif opsi == 'sakit' or opsi == 'izin' or opsi == 'hadir' or opsi == 'tanpa keterangan':
        jumlah_nama = tampilkan_data_berdasarkan_keterangan(opsi)
        print(f"\nJumlah nama dengan keterangan '{opsi}': {jumlah_nama}")
    elif opsi == 'absen':
        absen(keterangan)
    else:
        print("Perintah tidak valid")


os.system('clear' if os.name == 'posix' else 'cls')
