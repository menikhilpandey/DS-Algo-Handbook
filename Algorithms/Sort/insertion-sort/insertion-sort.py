# Written by @daydreamer at Oct 12, 2016. Trying to do same behaviour as the C code
# Except for the input part

sz = int(input('enter the number of elements to input:\n'))
ar = list(map(int, input('enter the elements:\n').split(' ')))

print("array before sorting:")
for item in ar:
    print(item)

for i in range(1, sz):
    temp = ar[i]
    j = i-1
    while ar[j] > temp and j >= 0:
        ar[j+1] = ar[j]
        j = j-1
    ar[j+1] = temp

print("array after sorting:")

for item in ar:
    print(item)

