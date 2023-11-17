nama_kelompok = []
npm_kelompok = []
n = int(input("Masukkan jumlah anggota kelompok: "))

for i in range(n):
    nama = input(f"Anggota ke-{i + 1}: ")
    npm = input(f"NPM anggota ke-{i + 1}: ")
    nama_kelompok.append(nama)
    npm_kelompok.append(npm)

for i, nama in enumerate(nama_kelompok):
    print(f"Anggota ke-{i+1}: {nama} ({npm_kelompok[i]})")
    for char in nama:
        print(char + "\n")
