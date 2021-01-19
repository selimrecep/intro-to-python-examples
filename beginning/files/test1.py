output = open('test1.txt', 'w')  # Needs to run in the same path 'test1.txt'
output.write('...\n')

list = ['legend\n', 'says\n', 'this\n', 'will\n',
        'not\n', 'be\n', 'that\n', 'painful\n']
output.writelines(list)

# This is NOT required, but see this: https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python#:~:text=Python%20automatically%20closes%20a%20file,method%20to%20close%20a%20file.
output.close()

# Default is 'R' mode if not specified
input = open('test1.txt')
lines = input.readlines()

# lines[i] contains new line character at the end
print(lines[0])
print(lines[1])
