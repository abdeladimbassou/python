l = [17, 38, 10, 25, 72, 45, 14]
print(l)
# Question numero 1 :
#   Methode 1
# for i in range(len(l)):
#    l[i] = l[i] + 1
# print(l)
#   Methode 2
for s in l:
    s += 1
    print(s)

# Question nº:2
l.extend([12, 13])
print(l)
# Question nº: 3
p = l.index(72)
# Question nº:4
print(p)
r1=[pair for pair in l if pair % 2 == 0]
print(r1)
r2=[imppair for imppair in l if imppair % 2 == 1]
print(r2)
# Question nº: 5
#   ** Methode 1  **
l = l[0:4] + [30] + l[4:]
#   ** Methode 2  **
# l.insert(4, 30)
print(l)
# Question nº: 6
l.remove(30)
print(l)
# Question nº: 7
l.reverse()
print(l)
# Question nº: 8
val = int(input('Donnez un nombre au hasard : '))
if val in l:
  print("%d est existe dans l ." % val)
else:
  print ("%d n'existe pas dans l." % val)
# Question nº: 9
print("la sous-liste du 2eme 3e élément", l[2:4])
# Question nº: 10
print("la sous-liste du début au 2eme élément", l[:3])
# Question nº:11
print("dernier element inversee est ", l[-1])


