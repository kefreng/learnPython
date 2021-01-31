with open('ejemplo_binary.bin','wb') as fw:
    fw.write(b'This is binary data....')

with open('ejemplo_binary.bin', 'rb') as f:
    print(f.read())


with open('ejemplo_text.txt','w') as fw:
    fw.write("texto ejemplo write\n")
    print("texto ejemplo write 2",file=fw)