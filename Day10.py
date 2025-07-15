x = input() # abc


def is_prime(num):
"""判斷一個數字是否為質數"""
if num <= 1:
return False
for i in range(2, int(num**0.5) + 1):
if num % i == 0:
return False
return True

def primes(n):
"""找出小於 n 的所有質數"""
    prime_list = []
for num in range(2, n):
if is_prime(num):
            prime_list.append(num)
return prime_list

while True:
try:
        x = int(input("請輸入一個整數 n: "))

if x <= 0:
print("請輸入大於零的正整數")
continue

        result = primes(x)
print(", ".join(map(str, result)))
break
except ValueError:

print("請輸入大於零的正整數")

except Exception as e:
print(f"發生了意外錯誤: {e}")
break

