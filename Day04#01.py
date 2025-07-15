L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s=[]

L[0:8]=[]
s.extend(L)
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.append(7)
s.append(8)

print(s) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
