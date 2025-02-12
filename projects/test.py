def input_matrix(rows, cols, nome):
    print(f"\nDigite os elementos da {nome}:")
    matriz = []
    for i in range(rows):
        linha = []
        for j in range(cols):
            elemento = int(input(f"Elemento na linha {i+1}, coluna {j+1}: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def print_matrix(matriz, nome):
    print(f"\n{nome}:")
    for linha in matriz:
        print(linha)

    # Obter dimensões da primeira matriz
    linhas1 = int(input("Digite o número de linhas da Matriz 1: "))
    colunas1 = int(input("Digite o número de colunas da Matriz 1: "))

    # Obter a primeira matriz
    matriz1 = input_matrix(linhas1, colunas1, "Matriz 1")

    # Obter dimensões da segunda matriz
    linhas2 = int(input("\nDigite o número de linhas da Matriz 2: "))
    colunas2 = int(input("Digite o número de colunas da Matriz 2: "))

    # Verificar se as dimensões são iguais
    if linhas1 != linhas2 or colunas1 != colunas2:
        print("\nErro: As matrizes devem ter as mesmas dimensões para serem somadas.")
    else:
        # Obter a segunda matriz
        matriz2 = input_matrix(linhas2, colunas2, "Matriz 2")

        # Calcular a soma das matrizes
        soma = []
        for i in range(linhas1):
            linha_soma = []
            for j in range(colunas1):
                linha_soma.append(matriz1[i][j] + matriz2[i][j])
            soma.append(linha_soma)
