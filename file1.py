nama_file = 'data.txt'

#windows
#nama_file = 'D:\\Android\\data.txt' D:\\alpro\\71220910-02\\namapanjang.py

#linux
#nama_file = '/var/www/data.txt'

handle = open(nama_file, 'w')
#read onl;y
#mode = r,w,a,b -> binary

#Mengambil baris tertentu
# n = 3
# no_baris = 1
# for baris in handle:
#     if no_baris == n:
#         print(baris)
#     no_baris = no_baris + 1
   
# handle.close
#1.Readlines => list
#2.read => semua baris
#3.readline => satu baris

# hasil = handle.readlines()
# keyword = input("Masukkan kata : ")
# hasil2 = 0
# for baris in hasil:
#     baris = baris.lower()
#     if keyword in baris:
#         hasil2 = hasil2 + 1
# print(hasil2)


