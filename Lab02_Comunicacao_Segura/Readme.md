# Lab02 - Comunicação Segura com Sockets UDP

Este projeto implementa um sistema de cliente e servidor utilizando o protocolo UDP em Python, focando nos pilares de **Confidencialidade** (via criptografia AES-256) e **Integridade** (via Hashing SHA-256).

##  Requisitos Técnicos
* **Linguagem:** Python 3.14
* **Biblioteca:** `cryptography` (Instalação via: `pip install cryptography`)
* **Protocolo:** UDP (Sockets `AF_INET`, `SOCK_DGRAM`)

##  Como Rodar a Atividade

Siga os passos abaixo exatamente nesta ordem para garantir que a comunicação funcione corretamente:

### 1. Preparação do Servidor
No primeiro terminal do VS Code:
1. Navegue até a pasta da atividade: `cd Lab02_Comunicacao_Segura`
2. Inicie o servidor: 
   ```powershell
   python UDPServer.py
   ```

   O servidor ficará em modo de espera exibindo a mensagem: "O servidor seguro está pronto para receber..."

## 2. Execução do Cliente

No segundo terminal do VS Code (ou terminal dividido):

1. Navegue até a mesma pasta: cd Lab02_Comunicacao_Segura

    Execute o cliente:
    ```powershell
    python UDPCliente.py
    ```

    Digite a mensagem desejada quando solicitado e aperte Enter.

 2. Verificação

    - O Cliente confirmará o envio e encerrará a execução.

    - O Servidor mostrará o endereço do cliente, confirmará se a integridade (Hash) está correta e exibirá a mensagem original após a descriptografia.

## Segurança Implementada

- AES-256 (Modo CBC): Garante que os dados trafeguem de forma cifrada.

- Vetor de Inicialização (IV): Gerado aleatoriamente para cada mensagem, impedindo padrões no texto cifrado.

- SHA-256: Gera um resumo digital (digest) do pacote para garantir que a mensagem não foi alterada no caminho.

- PKCS7 Padding: Garante que a mensagem tenha o tamanho correto para o bloco do algoritmo AES.