while True:
  n = int(input("請輸入正整數n(輸入0或負數離開)"))
if n<= 0:
print("結束程式")
break

  fact = 1
  total = 0

for k in range(1,n+1):
    fact *= k
    total += fact
print("1! + 2! + 3! + ... + n! 的總和:",total)
