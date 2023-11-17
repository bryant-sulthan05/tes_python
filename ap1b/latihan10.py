jawab = input("Tambah anggota kelompok? ")
kelompok = []
npm = []

while (jawab == 'ya'):
    nama_kelompok = input("Masukkan nama : ")
    npm_kelompok = input("Masukkan npm : ")
    kelompok.append(nama_kelompok)
    npm.append(npm_kelompok)
    for n, nama_k in enumerate(kelompok):
        print(f"{nama_k} ({npm[n]})")
    jawab = input("Tambah anggota? ")

    if jawab == 'tidak':
        break
print(f"Total anggota kelompok : {len(kelompok)}")
for i, nama in enumerate(kelompok):
    print(f"anggota ke-{i + 1} : {nama} ({npm[i]})")
