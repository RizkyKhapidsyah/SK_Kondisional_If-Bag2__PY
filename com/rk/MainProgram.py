from pip._vendor.distlib.compat import raw_input

# Created by Rizky Khapidsyah

print("Masukkan dua buah angka")
print("Dan Anda akan check hubungan kedua angka tersebut")

Angka1 = raw_input("Masukkan angka pertama : ")
Angka1 = int(Angka1)
Angka2 = raw_input("Masukkan angka kedua : ")
Angka2 = int(Angka2)

if Angka1 == Angka2:
    print("%d sama dengan %d" % (Angka1, Angka2))
else:
    print("%d tidak sama dengan %d" % (Angka1, Angka2))
