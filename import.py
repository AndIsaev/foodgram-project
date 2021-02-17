
n = ['Ulan', 'Sasha', 'Andy']

for i in n:
    print('Это был {}'.format(i))

k = 0

while k != len(n):
    k += 1
    print('Это был {}'.format(n[k-1]))


h = [{1 : 3}, {2 : 3}]
print(h[1])

f = [ 6, 7]
if 3 in f:
    print(3)
else:
    print(f'{3} нету')


