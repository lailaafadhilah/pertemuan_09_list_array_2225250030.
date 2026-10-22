def hitung_rata_rata(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)


def cari_nilai_tertinggi(data):
    if len(data) == 0:
        return None
    return max(data)


nilai = [70, 80, 90, 60, 85]

rata_rata = hitung_rata_rata(nilai)
tertinggi = cari_nilai_tertinggi(nilai)

print("Data nilai:", nilai)
print("Rata-rata:", f"{rata_rata:.2f}")
print("Nilai tertinggi:", tertinggi)

data_kosong = []
print("Rata-rata data kosong:",
      hitung_rata_rata(data_kosong))
