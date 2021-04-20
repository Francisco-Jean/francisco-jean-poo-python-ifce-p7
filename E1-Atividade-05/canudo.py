def canudinho(tam):
    ver1 = tam[0] + tam[1]
    ver2 = tam[0] + tam[2]
    ver3 = tam[1] + tam[2]

    if tam[0] <= 0 or tam[1] <= 0 or tam[2] <= 0:
        print("\nFalse")
    elif tam[2] >= ver1 or tam[1] >= ver2 or tam[0] >= ver3:
        print(f'\nOs comprimentos {tam} NÃO PODEM formar um triangulo!')
    else:
        print(f'\nOs comprimentos {tam} PODEM formar um triangulo!')

canudos = []

for x in range(3):
    canudos.append(int(input(f'Digite o tamanho do canudo {x+1}: ')))

canudinho(canudos)