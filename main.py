import numpy as np

data1 = [[3, 2, 6], [8, 5, 6], [19, 128, 9], [10, 11, 12]]
arr = np.array(data1)

print(arr)
print(type(arr))
print(arr.data)
print(arr.shape)
print(arr.dtype)
print(arr.itemsize)

a = np.zeros(10)
print(a)

b = np.ones(10)
print(b)

c = np.arange(1, 10 + 1)
print(c)

d = np.linspace(0, 1, 12)
print(d)

e = np.eye(4, 4, 1)
print(e)

print(arr * arr)
print(arr / 2)
print(1 / arr)
print(arr + 5)

h = np.random.randn(3, 5)
print(h)

v = np.random.randint(10, 20, 4)
print(v)

print(arr[0, 2])
print(arr[1:, 0])
print(arr[1:][0, 1])

names = ['Bob', 'Joe', 'Mikhail', 'Bob']
names_np = np.array(names)
print(names_np == 'Bob')

name_mask = (names_np == 'Joe') | (names_np == 'Mikhail')
print(names_np[name_mask])
print('<' * 30)

print(arr)
print(arr.T)

print(np.sqrt(arr))
print(np.exp(arr))
print('<' * 30)

print(arr.mean())
print(arr.sum())
print(arr.max())
print('<' * 30)

print(arr.cumsum(axis=0))
print('<' * 30)

print(arr)
arr.sort(0)
print(arr)

np.save(arr=arr, file='arr.npy')
loaded_arr = np.load(file='arr.npy')
print(loaded_arr)

print('<' * 30)
print('<' * 30)
print('task #1')
vec = np.arange(10, 500 + 1)
print(vec)
print('ans:', np.sum((vec ** 2) - 234))
