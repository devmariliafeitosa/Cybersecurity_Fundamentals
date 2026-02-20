from socket import *
import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

CHAVE = b"chave_secreta_com_32_caracteres!"
serverName = "127.0.0.1" 
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Digite a mensagem para enviar com segurança: ')
message_bytes = message.encode()

preenchedor = padding.PKCS7(128).padder()
message_padded = preenchedor.update(message_bytes) + preenchedor.finalize()

iv = os.urandom(16)
cifrador = Cipher(algorithms.AES(CHAVE), modes.CBC(iv))
config_cripto = cifrador.encryptor()
ciphertext = config_cripto.update(message_padded) + config_cripto.finalize()

hash_seguranca = hashlib.sha256(ciphertext).digest()

pacote_final = iv + hash_seguranca + ciphertext
clientSocket.sendto(pacote_final, (serverName, serverPort))

print("Mensagem criptografada enviada!")
clientSocket.close()