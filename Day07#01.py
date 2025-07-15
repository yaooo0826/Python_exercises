x = input("請輸入數字")

if x.isdigit(): #isdigit()方法偵測字串是否只由數字組成，只對 0 和 正數有效。
  y=int(x)
  n=1

for i in range(1,y+1):
    n*=i
print("n!=",n)

else:
print(x,"是一個不合法的輸入，無法運算")
