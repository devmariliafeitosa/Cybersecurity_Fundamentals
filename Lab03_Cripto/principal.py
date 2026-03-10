from funcoes_cripto import texto_para_binario_invertido, decifrar_texto
import random

print("--- SISTEMA DE CRIPTOGRAFIA ADS ---")

frase = input("Digite o texto que deseja cifrar: ")
chave = random.randint(1, 10)

resultado_cifrado = texto_para_binario_invertido(frase, chave)
print(f"\nChave aleatória utilizada: {chave}")
print(f"Texto Cifrado: {resultado_cifrado}")

print("-" * 30)

input("Pressione Enter para ver o texto original decifrado...")
original = decifrar_texto(resultado_cifrado, chave)
print(f"Texto Original: {original}")