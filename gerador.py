import csv
import random
import string

ARQUIVO_SAIDA = "megasena.csv"
QUANTIDADE_LINHAS = 1000

MIN_NUMEROS = 6
MAX_NUMEROS = 15


def gerar_identificador():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_linha():
    identificador = gerar_identificador()

    # Gera uma quantidade aleatória entre 6 e 15 números
    quantidade_numeros = random.randint(MIN_NUMEROS, MAX_NUMEROS)

    # Sorteia números únicos entre 1 e 60
    numeros = random.sample(range(1, 61), quantidade_numeros)

    # Ordena os números
    numeros.sort()

    return [identificador] + numeros


def linha_valida(linha):
    # A primeira posição é o ID
    numeros = linha[1:]

    # Valida quantidade de números
    if len(numeros) < MIN_NUMEROS or len(numeros) > MAX_NUMEROS:
        return False

    # Converte os números para inteiros
    try:
        numeros = [int(numero) for numero in numeros]
    except ValueError:
        return False

    # Valida se todos estão entre 1 e 60
    if not all(1 <= numero <= 60 for numero in numeros):
        return False

    # Valida números repetidos
    if len(numeros) != len(set(numeros)):
        return False

    return True


with open(ARQUIVO_SAIDA, "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    linhas_validas = 0
    linhas_descartadas = 0

    for _ in range(QUANTIDADE_LINHAS):

        linha = gerar_linha()

        if linha_valida(linha):
            escritor.writerow(linha)
            linhas_validas += 1
        else:
            linhas_descartadas += 1


print("Processamento concluído!")
print(f"Linhas válidas: {linhas_validas}")
print(f"Linhas descartadas: {linhas_descartadas}")
print(f"Arquivo gerado: {ARQUIVO_SAIDA}")