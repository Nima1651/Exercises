primes = []
start = int(input("start: "))
end = int(input("end: "))
for num in range(start, end+1):
    if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
        primes.append(num)
        


print(primes)
