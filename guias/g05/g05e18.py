s1 = {'a', 'e', 'i', 'o', 'u'}
s2 = 'mia'
s2 = set(s2)
print(s2)
if s1.intersection(s2) == s1:
    print('todas')
else:
    print('faltan')