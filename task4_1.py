def hash_key(v,m):
    return v%m
m=int(input('Enter the size of input list/number of all elements :'))
v=int(input('Enter the value :'))
print(f'the hash value is :{hash_key(v,m)}')
