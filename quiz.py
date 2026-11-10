print("=" * 42)
print("   QUIZ REMEDIAL UJIAN MATEMATIKA")
print("=" * 42)

nama = input("Masukkan nama mahasiswa (Andi/Budi/Citra): ")

if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0

if target == 0:
    print("Nama tidak terdaftar. Program dihentikan.")
else:
    print("Target nilai", nama, ":", target)
    print("-" * 42)

    percobaan = 1
    nilai = int(input("Nilai " + str(percobaan) + " : "))

    while nilai < target and percobaan < 3:
        print("Nilai belum mencapai target, ikuti remedial!")
        percobaan += 1
        nilai = int(input("Nilai " + str(percobaan) + " : "))

    print("-" * 42)
    if nilai >= target:
        print(nama, "berhasil lulus setelah", percobaan, "kali percobaan!")
    else:
        print(nama, "tidak lulus setelah", percobaan, "kali percobaan!")
