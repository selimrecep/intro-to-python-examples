# w+ Truncates whole file if doesn't exist, and starts reading/writing from beginning of the file
io = open('test2.txt', 'w+')
L = [9, 8, 7, 6]

io.write(str(L) + '\n')

io.write('Did you know that ')
io.write('the {} is the most strongest part in our bodies?'.format('femur') + '\n')
io.flush()

io.seek(2)
line = io.readline()
print(line + ' :)')
