with open('test4.txt', 'w') as file:
    file.write('hi')

with open('test4.txt', 'r') as file:
    print(file.read())
