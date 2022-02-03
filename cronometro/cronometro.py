import time

x = input('Quer contar até quantos? ')
x = int(x)
y = 0
g = 0
y = int(y)
a = 0

while g <= x:
    print(f'{a:0>2}:{y:0>2}')
    y = y + 1
    g = g + 1

    if y == 60:
        a = a + 1
        y = y - 60

    if g == x // 2:
        print('Ja foi metade do tempo')
    if g == x:
        print('Fim')

    time.sleep(0.008)

    #  github = LeonardoAlberto
