# List - Akses dan Manipulasi
print("--List - Akses dan Manipulasi--")    
data = ["mangga", 12, "stroberi", 7, "durian", 8, "melon"]
print("elemen pertama:", data[0])
print("elemen terakhir:", data[-1])
print("data slicing:", data[0:5:2]) # slicing dengan step 2 dengan start stop tertentu 
print("data slicing:", data[::2]) # slicing dengan step 2, mulai dari awal hingga akhir
print("data slicing:", data[1:6]) # slicing, step default 1
print("sebelum manipulasi:", data) #list sebelum dimanipulasi
data.append("manggis")
print("setelah append:", data) #list setelah append
data.insert(2, "leci")
print("setelah insert:", data) #list setelah insert
data.extend([100,"apel"])
print("setelah extend:", data) #list setelah extend
data.pop()
print("setelah pop:", data) #list setelah pop
data.remove("mangga")
print("setelah remove:", data) #list setelah remove

#Tuple – Immutability & Unpacking
print("\n--Tuple - Immutability & Unpacking--")
data_tuple = ("kangkung", 9, "bayam", 7, "selada", 2)
print("panjang tuple:", len(data_tuple)) #panjang tuple
print("elemen pertama:", data_tuple[0]) #akses indeks
print("elemen kedua terakhir:", data_tuple[-2]) #akses indeks
a, b, c, *rest = data_tuple
print("a:", a) #unpacking
print("b:", b) #unpacking   
print("c:", c) #unpacking   
print("rest:", rest) #unpacking 

#Set – Keunikan & Operasi Himpunan
print("\n--Set - Keunikan & Operasi Himpunan--")
set1 = {"mawar", "melati", "anggrek", "tulip", "teratai"}
set2 ={"lavender", "teratai", "mawar", "krisan", "lili"}
print("set1:", set1) #menampilkan set1
print("set2:", set2) #menampilkan set2
print("Union:", set1 | set2) #union
print("Intersection:", set1 & set2) #intersection
print("Difference:", set1 - set2)  #difference
print("Symmetric Difference:", set1 ^ set2) #symmetric difference
set_yg_duplikat = {"mawar", "teratai", "teratai", "mawar"}
print("input (ada duplikat): {'mawar', 'teratai', 'teratai', 'mawar'}") #menampilkan set dengan duplikat
print("output set tanpa duplikat:", set_yg_duplikat) #menampilkan set dengan duplikat yg otomatis hilang duplikatnya 

# Dictionary – Key/Value Dasar
print("\n--Dictionary - Key/Value Dasar--")
mahasiswa ={
    "Nama": "Jocelyn",
    "NIM": "1234567",
    "Angkatan": 2023,
    "Kota": "Batam"
}
print("Data Awal:", mahasiswa) #menampilkan dictionary awal
mahasiswa["Jurusan"] = "Sistem Informasi" #tambah key baru 
print("Setelah menambah key baru (Jurusan): ", mahasiswa)
mahasiswa["Kota"] = "Tanjungpinang" #ubah value pada key Kota
print("Setelah mengubah value pada key Kota: ", mahasiswa)
del mahasiswa["Angkatan"] #hapus key Angkatan
print("Setelah menghapus key Angkatan: ", mahasiswa)
print("Keys:", mahasiswa.keys()) #menampilkan semua key
print("Values:", mahasiswa.values()) #menampilkan semua value
print("Items:", mahasiswa.items()) #menampilkan semua item (key-value pairs)
print("\nData Mahasiswa:")
for key, value in mahasiswa.items(): #iterasi dictionary
    print(f"{key}: {value}")

# Nested structures
print("\n--Nested Structures--")
buku = [
    {"Judul": "Pulang", "Penulis": "Tere Liye", "Tahun": 2015},
    {"Judul": "Dilan 1990", "Penulis": "Pidi Baiq", "Tahun": 2014},
    {"Judul": "Laskar Pelangi", "Penulis": "Andrea Hirata", "Tahun": 2005},
    {"Judul": "Bumi", "Penulis": "Tere Liye", "Tahun": 2014},
    {"Judul": "Negeri 5 Menara", "Penulis": "Ahmad Fuadi", "Tahun": 2009},
    {"Judul": "Ayat-Ayat Cinta", "Penulis": "Habiburrahman El Shirazy", "Tahun": 2004}
]
for item in buku:
    print(item["Judul"])
buku_baru = [item for item in buku if item["Tahun"] >= 2010]
print("Buku yang diterbitkan pada atau setelah tahun 2010:")
for x in buku_baru:
    print(x["Judul"])

#Comprehension & Utilitas
print("\n--Comprehension & Utilitas--")
#List comprehension
angka = list(range(1, 21)) #list angka 1-20
list_genap = [x for x in angka if x % 2 == 0] #list angka genap
list_kuadrat = [x**2 for x in angka] #list kuadrat
print("List angka 1-20:", angka) #menampilkan list angka 1-20
print("List angka genap 1-20:", list_genap) #menampilkan list angka genap
print("List kuadrat 1-20:", list_kuadrat) #menampilkan list kuadrat
#Dict comprehension
angka_dict = {x:"genap" if x % 2 == 0 else "ganjil" for x in range (1,11)}
print("Mapping angka 1-10 ke genap/ganjil:", dict) #menampilkan mapping angka 1-10 ke genap/ganjil
#Set comprehension
kalimat = "Saya sedang membuat tugas Python"
huruf_unik = {x.lower() for x in kalimat if x.isalpha()}
print("Huruf unik:", huruf_unik)

# Keanggotaan & Pencarian Sederhana
print("\n--Keanggotaan & Pencarian Sederhana--")
list_buah = ["durian", "manggis", "melon", "jeruk", "apel"]
tuple_buah = ("durian", "manggis", "melon", "jeruk", "apel")
print("Apakah 'durian' ada di list ?", "durian" in list_buah) #pencarian dengan in pada list
print("Apakah 'melon' ada di tuple ?", "melon" in tuple_buah) #pencarian dengan in pada tuple
if "durian" in list_buah:
    print("posisi 'durian' di index:", list_buah.index("durian")) #pencarian dengan if in pada list
else:
    print("durian tidak ditemukan di list")