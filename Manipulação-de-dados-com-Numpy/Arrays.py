import numpy as np

# Array
arrayFloat = np.array([1, 2, 3.1], dtype=np.float32)
arrayString = np.array([1, 2, "3"])
print(repr(arrayFloat))
print(repr(arrayString))

# Copying
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a

print(f'Array a: {a}')
c[0] = 500
print(f'Array a: {a}')

print(f'Array b: {b}')
d = b.copy()
d[0] = 500
print(f'Array b: {b}')

# Casting
arr = np.array([1, 2, 3])
print(repr(arr))
arr = arr.astype(np.str)
print(repr(arr))

# NaN (Not a Number)
arr = np.array([np.nan, 1, 2])
print(repr(arr))

arr = np.array([np.nan, 'abc'])
print(repr(arr))

# Infinity
arr = np.array([np.inf, 1])
print(arr)

arr = np.array([-np.inf, 1])
print(arr)
