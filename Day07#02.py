L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_list = []
even_list = []

for x in L:
if x % 2 == 1:
    odd_list.append(x)
elif x % 2 ==0:
    even_list.append(x)

L=odd_list+even_list

print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

