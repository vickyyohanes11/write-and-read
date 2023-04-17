nama_file = 'data2.txt'
handle = open(nama_file,'w')

isifile = input("Kalimat baru : ")
handle.write(isifile)
print(isifile)