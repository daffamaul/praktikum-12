# String

```python
txt = "Hello World"
```
## Menghitung jumlah karakter
```python
print("jumlah karakter: ", len(txt))
```

## Mengambil elemen terakhir
```python
print("Elemen terakhir: ", txt[len(txt)-1])
```

## Mengambil karakter index ke-2 sampai index ke-4
```python
print("Elemen ke-2 sampai ke-4: ", txt[2:5])
```

## Hilangkan spasi pada teks tersebut
```python
print("Teks tanpa spasi: ", txt.replace(" ",""))
```

## Ubah teks menjadi huruf besar 
```python
print("Teks huruf besar: ", txt.upper())
```

## Ubah teks menjadi huruf kecil
```python
print("Teks huruf kecil: ", txt.lower())
```

## Ganti karakter H menjadi karakter J
```python
print("H menjadi J: ", txt.replace("H","J")
```

```python
umur = 24
txt = "Hello, nama saya adalah john, umur saya adalah {0} tahun"
print(txt.format(umur))
```
