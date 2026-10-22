nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
batas_lulus = 60

nilai_lulus = []
jumlah_tidak_lulus = 0

for n in nilai:
    if n >= batas_lulus:
        nilai_lulus.append(n)
    else:
        jumlah_tidak_lulus += 1

print("Data nilai:", nilai)
print("Batas kelulusan:", batas_lulus)
print("Nilai yang lulus:", nilai_lulus)
print("Jumlah lulus:", len(nilai_lulus))
print("Jumlah tidak lulus:", jumlah_tidak_lulus)
