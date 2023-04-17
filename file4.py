namafile = 'data3.txt'
handle = open(namafile,'r+')
isifile = handle.read()
isifile = isifile.lower()
print("Isi file sekarang")
print(isifile)
handle.close

katalama = input("Masukkan kata  : ")
katalama = katalama.lower()

if isifile.count(katalama) == 0:
    print("Tidak ada kata")
else:
    katabaru = input("Masukkan Kata Baru : ")
    katabaru = katabaru.lower()
    handle = open(namafile, 'w')
    isifile = isifile.replace(katalama,katabaru)
    handle.write(isifile)
    handle.close
