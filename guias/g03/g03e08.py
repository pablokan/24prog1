n = [1,2,3,4,5]

for i in range(len(n)//2):
    aux = n[i]
    #n[i] = n[len(n)-1-i]
    #n[len(n)-1-i] = aux
    n[i] = n[-1-i]
    n[-1-i] = aux
print(n)

