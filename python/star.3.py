def star(n):
    for i in range(1,n+1):
        print(" " *(n-i) + "*" * (3*i-1))
print(star(9))

