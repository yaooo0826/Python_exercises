x = input()

def isPrime(n):
    n = int(n)
if n < 2:
return False
if n==2:
return True
for i in range(2,n):
if n%i==0:
return False
return True

def primes(n):
    n = int(n)
    prime_list = []
if n == 1:
print("輸入為1，沒有質數")
elif n == 2:
print("輸入為2，沒有小於2的質數")
else:
for i in range(2,n):
if(isPrime(i)):
                prime_list.append(i)
print(prime_list)

primes(x)
