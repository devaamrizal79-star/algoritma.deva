print ("======NILAI MAHASISWA======")
nama_mhs = input("Nama Mahasiswa")
kelas = input("Kelas Mahasiswa")

nilai_a = int(input("Masukan Nilai Bahasa Indonesia :"))
nilai_b = int(input("Masukan Nilai Algoritma :"))
nilai_c = int(input("Masukan Nilai Pkn :"))
nilai_d = int(input("Masukan Nilai Basis Data :"))
nilai_e = int(input("Masukan Nilai Agama :"))
nilai_f = int(input("Masukan Nilai Informatika :"))
nilai_g = int(input("Masukan Nilai Bahasa Inggris :"))
rata_rata = (nilai_a + nilai_b + nilai_c + nilai_d + nilai_e + nilai_f + nilai_g) / 7

if rata_rata >=90 and rata_rata <100:
    print ("Nilai : A")
elif rata_rata >=80 and rata_rata <=90:
    print ("Nilai : B")
elif rata_rata >=70 and rata_rata <=80:
    print ("Nilai : C")
elif rata_rata >=60 and rata_rata <=70:
    print ("Nilai : D")
else:
    print ("nilai : E")

