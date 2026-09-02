import csv
import random
import string

ARQUIVO_SAIDA = "megasena.csv"
QUANTIDADE = 1000


def gerar_identificador():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=6))
    return f"AP-{codigo}"


with open(ARQUIVO_SAIDA, "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for _ in range(QUANTIDADE):
        identificador = gerar_identificador()

        # Sorteia 6 números diferentes entre 1 e 60
        numeros = random.sample(range(1, 61), 6)

        # Coloca os números em ordem crescente
        numeros.sort()

        escritor.writerow([identificador] + numeros)


print(f"Arquivo '{ARQUIVO_SAIDA}' criado com {QUANTIDADE} linhas.")
