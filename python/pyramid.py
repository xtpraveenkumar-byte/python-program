
def star(n):
    for i in range(n,0,-1):
        print(" " *(n-i) + "*" *(2*i-1))
print(star(9))
