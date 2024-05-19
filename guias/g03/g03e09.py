nombres = ['Ana', 'Luis', 'Lisa']
sueldos = [1_951_000, 727_000, 2_765_000]

for i in range(len(sueldos)):
    if sueldos[i] > 1_850_000:
        print(nombres[i])

