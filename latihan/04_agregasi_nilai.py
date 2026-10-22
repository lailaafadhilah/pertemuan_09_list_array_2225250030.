nilai = [75, 80, 65, 90, 85]

jumlah_data = len(nilai)
total = sum(nilai)
rata_rata = total / jumlah_data
nilai_minimum = min(nilai)
nilai_maksimum = max(nilai)

print("Data nilai:", nilai)
print("Jumlah data:", jumlah_data)
print("Total nilai:", total)
print("Rata-rata:", f"{rata_rata:.2f}")
print("Nilai minimum:", nilai_minimum)
print("Nilai maksimum:", nilai_maksimum)
