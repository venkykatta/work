n = int(input("Enter the number needed:"))

for i in range(1, n+1):
    print(' ' * n, end='')
    print('* ' * i)
    
    n -= 1