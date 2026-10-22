
def rata_rata(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    return [nilai for nilai in data if nilai >= batas]


def analisis_nilai(data, batas=60):
    print("Daftar nilai:", data)

    if len(data) == 0:
        print("Jumlah data: 0")
        print("Total nilai: 0")
        print("Rata-rata: Tidak ada data")
        print("Nilai minimum: Tidak ada data")
        print("Nilai maksimum: Tidak ada data")
        print("Daftar nilai lulus: []")
        print("Jumlah lulus: 0")
        print("Jumlah belum lulus: 0")
        return

    total = sum(data)
    rata = rata_rata(data)
    minimum = min(data)
    maksimum = max(data)

    daftar_lulus = nilai_lulus(data, batas)
    jumlah_lulus = len(daftar_lulus)
    jumlah_belum_lulus = len(data) - jumlah_lulus

    print("Jumlah data:", len(data))
    print("Total nilai:", total)
    print(f"Rata-rata: {rata:.2f}")
    print("Nilai minimum:", minimum)
    print("Nilai maksimum:", maksimum)
    print("Daftar nilai lulus:", daftar_lulus)
    print("Jumlah lulus:", jumlah_lulus)
    print("Jumlah belum lulus:", jumlah_belum_lulus)


def test_case():
    print("\n===== TEST CASE 1: RATA-RATA =====")
    data = [60, 70, 80]
    print("Data:", data)
    print(f"Rata-rata: {rata_rata(data):.2f}")
    print("Hasil yang diharapkan: 70.00")

    print("\n===== TEST CASE 2: MINIMUM / MAKSIMUM =====")
    print("Data:", data)
    print("Minimum:", min(data))
    print("Maksimum:", max(data))
    print("Hasil yang diharapkan: 60 / 80")

    print("\n===== TEST CASE 3: JUMLAH LULUS =====")
    print("Data:", data)
    print("Jumlah lulus:", len(nilai_lulus(data)))
    print("Hasil yang diharapkan: 3")

    print("\n===== TEST CASE 4: BATAS KELULUSAN =====")
    data = [59, 60, 61]
    print("Data:", data)
    print("Daftar nilai lulus:", nilai_lulus(data))
    print("Jumlah lulus:", len(nilai_lulus(data)))
    print("Hasil yang diharapkan: 2 lulus")

    print("\n===== TEST CASE 5: DATA KOSONG =====")
    data = []
    hasil = rata_rata(data)

    if hasil is None:
        print("Rata-rata: Tidak ada data")
        print("Penanganan data kosong berhasil.")
        print("Hasil yang diharapkan: Tidak error")
    else:
        print("Rata-rata:", hasil)


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

print("===== ANALISIS NILAI MAHASISWA =====")
analisis_nilai(nilai, batas=60)

test_case()
