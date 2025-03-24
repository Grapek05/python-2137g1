def prime_sieve(n: int):
    m = n +1
    numbers = [True] * m
    numbers[0] = False
    numbers[1] = False
    

    for i in range(2,int(m**0.5)):
        if numbers[i] == True:
            for j in range(i*i,m,i):
                numbers[j] = False
    
    for i,v in enumerate(numbers):
        if v == True:
            print(i)

prime_sieve(100)