import random

def texto_para_binario_invertido(texto, chave_aleatoria):
    texto_cifrado = ""
    
    for caractere in texto:

        numero = ord(caractere) + chave_aleatoria
        binario = bin(numero)[2:].zfill(8)
        binario_invertido = ""
        for bit in binario:
            if bit == '0':
                binario_invertido += '1'
            else:
                binario_invertido += '0'
        
      
        decimal_novo = int(binario_invertido, 2)
        texto_cifrado += chr(decimal_novo)
        
    return texto_cifrado

def decifrar_texto(texto_cifrado, chave_aleatoria):
    texto_original = ""
    
    for caractere in texto_cifrado:
        binario_invertido = bin(ord(caractere))[2:].zfill(8)
        binario_original = ""
        for bit in binario_invertido:
            if bit == '1':
                binario_original += '0'
            else:
                binario_original += '1'
        decimal = int(binario_original, 2) - chave_aleatoria
        texto_original += chr(decimal)
        
    return texto_original