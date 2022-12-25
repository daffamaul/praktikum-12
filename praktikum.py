# Menghtiung jumlah karakter
txt = 'Hello World'
print("Jumlah karakter = ", len(txt))

# Ambil karakter terkahir
print("Elemen terakhir = ", txt[len(txt)-1])

# Ambil karakter ke-2 sampai index ke-4 
print("Elemen ke-2 sampai ke-4 = ", txt[2:5])

# Hilangkan spasi pada teks tersebut
print("Teks tanpa spasi = ", txt.replace(" ",""))

# Ubah teks menjadi huruf besar
print("Teks besar = ", txt.upper())

# Ubah teks menjadi huruf kecil
print("Teks besar = ", txt.lower())

# Ganti karakter H dengan karakter J
print("H menjadi J = ", txt.replace("H","J"))

umur = 24
txt = 'Hello, nama saya adalah john, umur saya adalah {0} tahun'
print(txt.format(umur))
