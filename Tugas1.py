# Input data mahasiswa
tugas = float(input("Nilai tugas : "))
uts = float(input("Nilai UTS   : "))
uas = float(input("Nilai UAS   : "))
kehadiran = float(input("Kehadiran   : "))

# Hitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

# Ekspresi logika untuk syarat
lulus = nilai_akhir >= 75 and kehadiran >= 80
predikat = nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0

# Tentukan status
if predikat:
    status = "LULUS DENGAN PREDIKAT"
if lulus and not predikat:
    status = "LULUS"
if not lulus:
    status = "BELUM LULUS"

# Tampilkan output
print("Nilai Akhir :", nilai_akhir)
print("Status      :", status)