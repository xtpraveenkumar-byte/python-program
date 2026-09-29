def chekprime(check):
    count=0
    for i in range(1,check+1):
        if check % i ==0:
            count+=1
    if count ==2:
        print("the number is prime")
    else:
        print("not the prime number")

chekprime(12)


