n = int(input('Enter the number rows needed:'))

# for i in range(0, n):
#     for j in range(0, i+1):
#         print(i, end='')
#     print('\n')


for i in range(n):
    for j in range(i+1):
        print(j+1, end = '')
    print('\n')
    
    