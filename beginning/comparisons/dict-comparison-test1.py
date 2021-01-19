fibonacci = {'num1': 1, 'num2': 1, 'num3': 2, 'num4': 4}
nums = {'num1': 1, 'num2': 2, 'num3': 3, 'num4': 4}

print(sorted(fibonacci.items()) > sorted(nums.items()))

print(sorted(fibonacci.items()) < sorted(nums.items()))

print(fibonacci.items(), '--', sorted(fibonacci.items()))
print(nums.items(), '--', sorted(nums.items()))
# Hmm, it seems like sorted converts from 'dict_items' to a native list!
