def star(n):
    for i in range(1,n+1):
        print(" " *(n-i) + "*" * (2*i))
print(star(9))

