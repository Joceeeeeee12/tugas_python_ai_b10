#Deklarasi Variabel dan Tipe Data 
nama = "Jocelyn" #string
umur = 20 #integer
tinggi = 1.59 #float
is_CollegeStudent = True #boolean
hobi = ["nyanyi", "badminton", "nonton"] #list
tanggal_lahir = (12, "Juli", 2005) #tuple

print("--Deklarasi Variabel dan Tipe Data--")
print(nama) #string
print(umur) #integer
print(tinggi) #float
print(is_CollegeStudent) #boolean
print(hobi) #list
print(tanggal_lahir) #tuple

#Manipulasi String
kalimat = "saya sedang membuat tugas python"
print("\n--Manipulasi String--")
print( kalimat) #print biasa
print(kalimat + " untuk tugas 3") #gabung string
print(len(kalimat)) #panjang string
print(kalimat.upper()) #huruf besar
print(kalimat.lower()) #huruf kecil
print(kalimat.replace("a", "i")) #mengganti kata / karakter 

#Operasi Matematika Sederhana
a = 10 
b = 3
print("\n--Operasi Matematika Sederhana--")
print(a+b) #penjumlahan
print(a-b) #pengurangan
print(a*b) #perkalian
print(a/b) #pembagian dengan hasil float
print(a//b) #pembagian bulat
print(a%b) #modulus

#List dan Akses Elemen
buah = ["apel", "jeruk", "pisang", "mangga", "anggur"]
print("\n--List Buah--")
print(buah) #print list
print(buah[0]) #ak elemen pertama
print(buah[-1]) #tampilkan elemen terakhir
buah.append("melon")
print(buah) #menambahkan elemen baru ke akhir list
buah.remove("jeruk")
print(buah) #menghapus elemen pertama dengan nilai tertentudari list
buah.pop(1)
print(buah) #menghapus elemen tertentu dari list berdasarkan indeks

#Input Dari User
print("\n--Input Dari User--")
while True:
    nama_user = input("Masukkan nama Anda: ").strip() #input nama 
    if nama_user !="":
        nama_user = nama_user.capitalize()
        break
    print("nama tidak boleh kosong")

while True:
    umur_user = input("Masukkan umur Anda: ").strip() #input umur
    if umur_user.isdigit():
        break
    print("umur harus angka dan tidak boleh kosong")
print("Hi, nama saya adalah", nama_user, "dan umur saya", umur_user, "tahun.")



