# Pertemuan 09 - List/Array dan Pengolahan Data Numerik Sederhana

**Nama:** Laila Fadhilah
**NIM:** 2225250030  
**Kelas:** 3A

## Tujuan

Memahami penggunaan list atau array dalam Python untuk menyimpan dan mengolah data numerik. Kegiatan meliputi pembuatan list, penggunaan indeks dan slicing, manipulasi list, perhitungan statistik sederhana, penyaringan nilai berdasarkan batas kelulusan, serta penggunaan fungsi.

## Cara Menjalankan

**Algoritma dan Pemrograman | Pertemuan 09**

Program dijalankan menggunakan Python 3 melalui terminal Visual Studio Code (VS Code).

Perintah untuk menjalankan setiap latihan:

```bash
python3 latihan/01_buat_list.py
python3 latihan/02_indeks_slicing.py
python3 latihan/03_manipulasi_list.py
python3 latihan/04_agregasi_nilai.py
python3 latihan/05_filter_kelulusan.py
python3 latihan/06_fungsi_statistik.py
```

Perintah untuk menjalankan tugas praktik utama:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

## Algoritma

1. Membuat list yang berisi beberapa data numerik.
2. Mengakses elemen list menggunakan indeks dan slicing.
3. Menambahkan, mengubah, dan menghapus elemen list.
4. Menghitung jumlah data, total nilai, rata-rata, nilai minimum, dan nilai maksimum.
5. Memeriksa setiap nilai menggunakan perulangan.
6. Menentukan kelulusan dengan batas nilai minimal 60.
7. Memasukkan nilai yang memenuhi batas kelulusan ke dalam list baru.
8. Menghitung jumlah nilai lulus dan tidak lulus.
9. Memeriksa apakah list kosong sebelum menghitung rata-rata.
10. Menampilkan hasil pengolahan data ke layar.

## Test Case

Berikut tabel Test Case yang lebih rapi untuk langsung kamu salin ke `README.md`.

## Test Case

| No. | Data           | Hasil yang Diperiksa                         | Hasil yang Diharapkan | Hasil Aktual          | Status   |
| --- | -------------- | -------------------------------------------- | --------------------- | --------------------- | -------- |
| 1   | `[60, 70, 80]` | Rata-rata                                    | `70.00`               | `70.00`               | Berhasil |
| 2   | `[60, 70, 80]` | Nilai minimum dan maksimum                   | `60 / 80`             | `60 / 80`             | Berhasil |
| 3   | `[60, 70, 80]` | Jumlah nilai lulus                           | `3`                   | `3`                   | Berhasil |
| 4   | `[59, 60, 61]` | Kelulusan dengan batas nilai 60              | `2 lulus`             | `2 lulus`             | Berhasil |
| 5   | `[]`           | Penanganan data kosong pada fungsi rata-rata | Tidak error           | Data kosong ditangani | Berhasil |

## Refleksi

Hal yang saya pahami dari penggunaan list adalah list dapat menyimpan banyak nilai dalam satu variabel sehingga data lebih mudah diolah menggunakan fungsi seperti `len()`, `sum()`, `min()`, dan `max()`.

Kesalahan yang berhasil diperbaiki adalah penanganan list kosong ketika menghitung rata-rata. Jika list kosong langsung dihitung, program dapat mengalami kesalahan pembagian dengan nol. Untuk mengatasinya, program memeriksa panjang list terlebih dahulu sehingga data kosong dapat ditangani tanpa menyebabkan program berhenti karena error.

