def f(*nums):
    total = 0
for num in nums:
        total += num
return total

print(f(1, 2, 3))
print(f(1, 2, 3, 4, 5))
