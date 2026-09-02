import csv
import random
import string
import sys

ARQUIVO_SAIDA = "saida.csv"

MIN_NUMEROS = 6
MAX_NUMEROS = 15


def gerar_identificador():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


def gerar_linha():
    identificador = gerar_identificador()

    # Gera entre 6 e 15 números
    quantidade_numeros = random.randint(MIN_NUMEROS, MAX_NUMEROS)

    # Sorteia números únicos entre 1 e 60
    numeros = random.sample(range(1, 61), quantidade_numeros)

    numeros.sort()

    return [identificador] + numeros


def linha_valida(linha):
    # Ignora o ID e considera somente os números
    numeros = linha[1:]

    # Verifica a quantidade de números
    if len(numeros) < MIN_NUMEROS or len(numeros) > MAX_NUMEROS:
        return False

    try:
        numeros = [int(numero) for numero in numeros]
    except ValueError:
        return False

    # Verifica se os números estão entre 1 e 60
    if not all(1 <= numero <= 60 for numero in numeros):
        return False

    # Verifica números repetidos
    if len(numeros) != len(set(numeros)):
        return False

    return True


def main():

    # Verifica se foi informado o argumento
    if len(sys.argv) != 2:
        print("Uso: python programa.py <quantidade_de_linhas>")
        sys.exit(1)

    # Converte o argumento para inteiro
    try:
        quantidade_linhas = int(sys.argv[1])
    except ValueError:
        print("Erro: a quantidade de linhas deve ser um número inteiro.")
        sys.exit(1)

    # Verifica se é maior que zero
    if quantidade_linhas <= 0:
        print("Erro: a quantidade de linhas deve ser maior que zero.")
        sys.exit(1)

    linhas_validas = 0
    linhas_descartadas = 0

    with open(
        ARQUIVO_SAIDA,
        "w",
        encoding="utf-8",
        newline=""
    ) as arquivo:

        escritor = csv.writer(arquivo)

        for _ in range(quantidade_linhas):

            linha = gerar_linha()

            if linha_valida(linha):
                escritor.writerow(linha)
                linhas_validas += 1
            else:
                linhas_descartadas += 1

    print("Processamento concluído!")
    print(f"Linhas solicitadas: {quantidade_linhas}")
    print(f"Linhas válidas: {linhas_validas}")
    print(f"Linhas descartadas: {linhas_descartadas}")
    print(f"Arquivo gerado: {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()