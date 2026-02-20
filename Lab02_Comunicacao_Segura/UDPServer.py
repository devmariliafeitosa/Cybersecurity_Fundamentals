from socket import *
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# PARÂMETROS ACORDADOS
CHAVE = b"chave_secreta_com_32_caracteres!"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("O servidor seguro está pronto para receber...")

while True:
    # 1. Recebe os dados (IV + HASH + MENSAGEM)
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # 2. Separação dos componentes
    iv = message[:16]
    hash_recebido = message[16:48]
    ciphertext = message[48:]

    # 3. VERIFICAÇÃO DE INTEGRIDADE
    hash_calculado = hashlib.sha256(ciphertext).digest()
    
    if hash_calculado == hash_recebido:
        # 4. DESCRIPTOGRAFIA
        cifrador = Cipher(algorithms.AES(CHAVE), modes.CBC(iv))
        descriptografador = cifrador.decryptor()
        dados_com_padding = descriptografador.update(ciphertext) + descriptografador.finalize()

        # 5. REMOVER PREENCHIMENTO (Unpadding)
        removedor = padding.PKCS7(128).unpadder()
        mensagem_final = removedor.update(dados_com_padding) + removedor.finalize()

        print(f"Mensagem recebida de {clientAddress}: {mensagem_final.decode()}")
    else:
        print("Aviso: Mensagem descartada! Falha na integridade.")