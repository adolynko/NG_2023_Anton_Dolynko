userInput = int(input())

for number in range(1, userInput + 1):
    array = []
    
    for num in range(1, number + 1):
        if number % num == 0:
            array.append(num)
    print(number, array)
    
primes = []
for num in range(2, userInput + 1):
    isPrime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(num)
print(primes)