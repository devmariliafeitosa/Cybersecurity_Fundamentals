import hashlib
import random
import time
import string


def gerar_md5(texto):
    texto_bytes = texto.encode()
    resultado = hashlib.md5(texto_bytes)
    return resultado.hexdigest()


def testar_conjunto(nome, conjunto):
    print("\n==============================")
    print("Testando:", nome)
    print("Total de símbolos:", len(conjunto))
    print("==============================")

    tempos = []

    for tentativa in range(1, 11):

        letra_secreta = random.choice(conjunto)

        hash_secreto = gerar_md5(letra_secreta)

        inicio = time.time()

        for letra in conjunto:

            hash_teste = gerar_md5(letra)

            if hash_teste == hash_secreto:
                break

        fim = time.time()

        tempo_gasto = fim - inicio
        tempos.append(tempo_gasto)

        print("Tentativa", tentativa)
        print("Letra:", letra_secreta)
        print("Tempo:", round(tempo_gasto, 6), "segundos")
        print("----------------------")

    media = sum(tempos) / len(tempos)

    print("Tempo médio:", round(media, 6), "segundos")
    print("==============================\n")


def main():

    minusculas = string.ascii_lowercase

    minusculas_maiusculas = string.ascii_letters

    todos = string.printable

    testar_conjunto("Somente letras minúsculas", minusculas)

    testar_conjunto("Minúsculas e maiúsculas", minusculas_maiusculas)

    testar_conjunto("Todos os caracteres", todos)


main()