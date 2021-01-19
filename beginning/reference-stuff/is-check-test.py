a = [5]
b = [5]

print(a == b, a is b)
# True, False

# Here comes the weird part :)
a = 1
b = 1
print(a == b, a is b)
# True, True. Surprising, isn't it? Python seems like keeping some small values like same object.

a = 2
print(a == b, a is b)
# False, False
