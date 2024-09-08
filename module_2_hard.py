password = ''
n = int(input('введите целое число от 3 до 20: '))
if n >= 3 and n <= 20:
    for i in range(1, n):
        for k in range(i, n):
            if i != k:
                if n % (i + k) == 0:
                    password += str(i)
                    password += str(k)
    print(n, '-', password)
else:
    print('извините, число не входит в указанный диапазон')
