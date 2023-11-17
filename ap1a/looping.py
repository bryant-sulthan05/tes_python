def hitung_suara(kandidat, suara):
    """
    Fungsi ini menghitung suara untuk setiap kandidat.
    """
    if suara.lower() in kandidat:
        kandidat[suara.lower()] += 1
    else:
        print("Kandidat tidak valid.")

def tampilkan_hasil(kandidat):
    """
    Fungsi ini menampilkan hasil pemilihan.
    """
    print("Hasil pemilihan:")
    for nama, jumlah_suara in kandidat.items():
        print(f"{nama.capitalize()}: {jumlah_suara} suara")

def main():
    # Data kelompok
    anggota_kelompok_6 = ['Arief Rahman (50423203)', 'Lahdar Bellumi (50423707)', 'Ridwan Kamil (50423993)', 'Rifki Zulkarnain (51423299)']
    anggota_kelompok_8 = ['Bryant Sulthan Nugroho (50423286)', 'Farrel Amri Bustomi(50423464)', 'Muhammad Yusuf Ghazali(51423033)', 'Raihanadri Putra Sarel(51423212)']

    # Gabungkan kedua kelompok
    anggota_kelompok = anggota_kelompok_6 + anggota_kelompok_8

    # Daftar kandidat
    kandidat = {"elang": 0, "abdul": 0, "zaid": 0}

    # Proses pemilihan untuk setiap anggota kelompok
    for anggota in anggota_kelompok:
        print(f"\n{anggota}, silakan memilih:")
        print("Pilih kandidat: Elang, Abdul, atau Zaid")
        pilihan = input("Masukkan pilihan: ")

        # Memastikan input sesuai
        while pilihan.lower() not in ["elang", "abdul", "zaid"]:
            print("Pilihan tidak valid. Silakan pilih kandidat Elang, Abdul, atau Zaid.")
            pilihan = input("Masukkan pilihan: ")

        # Menghitung suara
        hitung_suara(kandidat, pilihan)

    # Menampilkan hasil pemilihan
    tampilkan_hasil(kandidat)

main()