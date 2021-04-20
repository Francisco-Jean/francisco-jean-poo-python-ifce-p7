lados = []

for x in range(3):
    lados.append(int(input(f'Digite o comprimento do lado {x+1}: ')))

if lados[0] == lados[1] and lados[1] != lados[2] or lados[0] == lados[2] and lados[2] != lados[1] or lados[2] == lados[1] and lados[1] != lados[0]:
    print(f"\nO Triângulo com os lados {lados} é isósceles!\n")
elif lados[0] == lados[1] and lados[0] == lados[2]:
    print(f"\nO Triângulo com os lados {lados} é equilátero!\n")
else:
    print(f"\nO Triângulo com os lados {lados} é escaleno!\n")