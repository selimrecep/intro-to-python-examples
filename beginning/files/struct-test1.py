import struct

file = open('struct1.bin', 'wb')

data = struct.pack('>i1si', 18, b'.', 23)
file.write(data)

file.close()

file = open('struct1.bin', 'rb')
data = file.read()
obj = struct.unpack('>i1si', data)

# It prints like 18b'.'23 ... hmm
print(str(obj[0]) + str(obj[1]) + str(obj[2]))
