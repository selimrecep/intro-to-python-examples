io = open('test3.txt', 'w+')
io.write(str([1, 2, 3]).replace('[', '').replace(']', ''))

io.flush()

io.seek(0)

splits = io.readline().split(',')
nums = [int(P) for P in splits]
print(nums)
