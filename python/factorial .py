# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is undefined for negative numbers.")

#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# num = int(input("Enter a number: "))
# print(f"The factorial of {num} is {factorial(num)}")


def fact(n):
    result = 1
    for i in range(1,n+1):
        result =result * i
    return result


x=fact(5)
print(x)





