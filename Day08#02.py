while True:
  x = input("請輸入一組字串(輸入'q'則離開)")
if x == "q":
break

  char_counts = {}
for char in x:
if char in char_counts:
      char_counts[char] += 1
else:
      char_counts[char] = 1

print(char_counts)
