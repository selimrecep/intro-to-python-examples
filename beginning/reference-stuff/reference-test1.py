L = ['2020'] * 5
Years = [2019, L, 2021]

print(Years)
print('-------------------------------')
L[0] = None
print(Years)

print('--------- copying (not fullly, i.e., top-level copy) -------')
NewYears = Years[:]
L[0] = 'XXXX'
Years[0] = 'PPPP'
print(NewYears)
