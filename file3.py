namafile = 'data2.txt'
handle = open(namafile,'r')
isifile = handle.read()
print("Isi file sekarang")
print(isifile)
handle.close

enter = True
if isifile[-1] == '\n':
    enter = False
    

tambah = input("Masukkan kata baru : ")
if enter:
    tambah = '\n' + tambah

handle = open(namafile, 'a')
handle.write(tambah)
handle.close