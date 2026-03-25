# Laporan Tugas Python AI (Tugas 4, 5, dan 6)

## Deskripsi
Repository ini berisi kumpulan tugas pemrograman Python yang mencakup struktur data, function, object-oriented programming (OOP), serta pengolahan data menggunakan NumPy dan Pandas.

---

## Tugas 4 – Struktur Data Python
Pada tugas ini dipelajari berbagai struktur data dasar dalam Python.

### List
List = struktur data untuk menyimpan banyak nilai yang bisa diubah (mutable)
* Akses elemen = mengambil data berdasarkan index (menggunakan `[]`)
* Slicing = mengambil sebagian data (menggunakan `[start:stop:step]`)
* append() = menambahkan elemen ke akhir list
* insert() = menambahkan elemen pada posisi tertentu
* extend() = menambahkan banyak elemen sekaligus
* pop() = menghapus elemen terakhir
* remove() = menghapus elemen berdasarkan nilai

### Tuple
Tuple = struktur data untuk menyimpan nilai yang tidak bisa diubah (immutable)
* Tuple = struktur data yang tidak dapat diubah (immutable)
* Akses elemen = menggunakan index
* Unpacking = memisahkan isi tuple ke dalam beberapa variabel

### Set
Set = kumpulan data unik (tidak ada duplikasi)  
* Set = kumpulan data unik (tidak ada duplikasi)
* Union = menggabungkan dua set (`|`)
* Intersection = mengambil elemen yang sama (`&`)
* Difference = mengambil selisih elemen (`-`)
* Symmetric Difference = elemen yang tidak sama (`^`)

### Dictionary
Dictionary = struktur data pasangan key (kunci) dan value (nilai)
* Dictionary = struktur data key-value
* Menambah data = menambahkan pasangan key dan value
* Mengubah data = mengganti value pada key tertentu
* Menghapus data = menggunakan `del`
* Iterasi = menampilkan seluruh key dan value

### Nested Structure
Nested structure = struktur data yang berisi struktur data lain (misalnya list di dalam dictionary)
* Nested structure = struktur data di dalam struktur lain (contoh: list of dictionary)
* Filtering data = memilih data berdasarkan kondisi

### Comprehension
Comprehension = cara singkat membuat list, set, atau dictionary dalam satu baris kode
* List comprehension = membuat list secara ringkas
* Dict comprehension = membuat dictionary secara ringkas
* Set comprehension = membuat set secara ringkas

### Kesimpulan Tugas 4
Memahami berbagai struktur data dan cara penggunaannya untuk menyimpan serta memanipulasi data secara efisien.

---

## Tugas 5 – Function dan OOP
### Function
Function = blok kode yang dapat digunakan kembali untuk menjalankan tugas tertentu
* Function = blok kode yang dapat digunakan kembali
* greet() = menampilkan pesan salam
* tambah() = melakukan penjumlahan dengan parameter default
* rata_rata() = menghitung rata-rata dari list
* Validasi data = menangani kondisi list kosong

### Class (OOP)
Class (OOP) = blueprint untuk membuat object yang berisi data (atribut) dan fungsi (method)
* Class = blueprint untuk membuat object
* Object = hasil dari class yang dapat digunakan
Contoh dalam tugas :
Class `Student`:
* Atribut = nama, nim, nilai
* tambah_nilai() = menambahkan nilai ke dalam list
* rata_nilai() = menghitung rata-rata nilai
* status() = menentukan lulus atau tidak
* **str**() = menampilkan informasi object dalam bentuk string

### Kesimpulan Tugas 5
Function membantu membuat kode lebih modular, sedangkan OOP membantu mengelola data dan logika program secara terstruktur.

---

## Tugas 6 – NumPy, Pandas, File I/O, dan OOP
### Import & Setup
Import & Stepup adalah tahap awal untuk menyiapkan library (seperti NumPy dan Pandas) dan konfigurasi yang dibutuhkan sebelum program dijalankan.

### NumPy
NumPy = library Python untuk mengolah data numerik (angka) dalam bentuk array dengan cepat dan efisien.
* Array = struktur data numerik
* mean() = menghitung rata-rata
* median() = menghitung nilai tengah
* std() = menghitung standar deviasi
* min() = nilai minimum
* max() = nilai maksimum

### Pandas
Pandas = library Python yang digunakan untuk mengelola, memanipulasi, dan menganalisis data terstruktur seperti tabel (baris dan kolom)
* DataFrame = tabel data (baris dan kolom)
* Menambahkan kolom = membuat kolom baru (Status)
* Filtering = memilih data berdasarkan kondisi
* head() = menampilkan 5 data pertama

### File I/O
File I/O = proses membaca (input) dan menulis (output) data ke dalam file.
* open() = membuka file
* mode 'w' = menulis dan menimpa file
* mode 'a' = menambahkan isi ke file
* write() = menulis data ke file

### OOP – GradeBook
OOP (Object-Oriented Programming) = konsep pemrograman yang mengorganisir kode dalam bentuk object (objek) yang memiliki data dan fungsi.
* average() = menghitung rata-rata nilai
* pass_rate() = menghitung persentase kelulusan
* save_summary() = menyimpan ringkasan ke file
* **str**() = menampilkan ringkasan object

### Kesimpulan Tugas 6
Menggabungkan pengolahan data dan OOP untuk menghasilkan program yang terstruktur serta mampu menyimpan hasil ke dalam file.

---

## Kesimpulan Akhir
Dari tugas 4, 5, dan 6 dapat disimpulkan:
* Struktur data digunakan untuk menyimpan dan mengelola data
* Function membantu membuat kode lebih efisien dan reusable
* OOP membantu mengorganisir program dalam bentuk object
* NumPy dan Pandas mempermudah analisis data
* File I/O digunakan untuk menyimpan hasil program

---

## Penutup
Ketiga tugas ini membantu memahami dasar hingga menengah dalam Python, terutama dalam pengolahan data dan penerapan konsep OOP.
