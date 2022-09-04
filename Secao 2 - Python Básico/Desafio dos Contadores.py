a = 0
b = 10
for c in range(1, 10):
    print(f'{a} {b}')
    a += 1
    b -= 1

for p, r in enumerate(range(10, 1, -1)):
    print(f'{p} {r}')