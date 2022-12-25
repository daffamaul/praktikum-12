# String

```python
txt = "Hello World"
```
## Menghitung jumlah karakter
```python
print("jumlah karakter: ", len(txt))
```
![gambar1](/img/1.png)

## Mengambil elemen terakhir
```python
print("Elemen terakhir: ", txt[len(txt)-1])
```
![gambar2](/img/2.png)

## Mengambil karakter index ke-2 sampai index ke-4
```python
print("Elemen ke-2 sampai ke-4: ", txt[2:5])
```
![gambar3](/img/3.png)

## Hilangkan spasi pada teks tersebut
```python
print("Teks tanpa spasi: ", txt.replace(" ",""))
```
![gambar4](/img/4.png)

## Ubah teks menjadi huruf besar 
```python
print("Teks huruf besar: ", txt.upper())
```
![gambar5](/img/5.png)

## Ubah teks menjadi huruf kecil
```python
print("Teks huruf kecil: ", txt.lower())
```
![gambar6](/img/6.png)

## Ganti karakter H menjadi karakter J
```python
print("H menjadi J: ", txt.replace("H","J")
```
![gambar7](/img/7.png)

```python
umur = 24
txt = "Hello, nama saya adalah john, umur saya adalah {0} tahun"
print(txt.format(umur))
```
![gambar8](/img/8.png)
