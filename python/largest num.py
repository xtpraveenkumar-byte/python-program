def checks(n):
    largest= max(n)
    n.remove(largest)
    return max(n)

print(checks(n=[12,32,4,3]))


# a=[10,45,65,23,54]
# def p(a):
#     largest= max(a)
#     a.remove(largest)
#     return max(a)
# r=p(a)
# print("third largest: ",r)


# l=[23,34,55,67,89]
# print(sum(l))

