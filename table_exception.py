limit = int(input('Enter limit of addition: '))
size = int(input('Enter size of the table: '))
exception = int(input('Enter exception of addition: '))

print('\n\t Addition Table')
print('    |', end='')
for i in range(1, size + 1):
    print(format(i, '4d'), end=' ')
print('\n------------------------------------------------------------------')
for i in range(1, size + 1):
    print(i, end='\t|')
    for j in range(1, size + 1):
        if (j + i) == exception:
            print(format('', '4s'), end=' ')
        elif (j+i) <= limit:
            print(format(j + i, '4d'), end=' ')
        else:
            print(format('', '4s'), end=' ')
    print()

