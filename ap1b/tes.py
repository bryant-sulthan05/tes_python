def nilai():
    nama = "Bryant"
    npm = 50423286
    nilai = int(input("Masukkan nilai: "))

    print("\nHasil UTS Anda...")
    print(f"Nama: {nama}")
    print(f"Npm: {npm}")
    print(f"Nilai: {nilai}")
    if nilai > 75:
        print("Anda Lulus")
    else:
        print("Anda Remedial\n")

        remed = int(input("Masukkan nilai remedial: "))
        if remed >= 75:
            print("Anda Lulus")
        else:
            print("Anda Tidak Lulus")
nilai()