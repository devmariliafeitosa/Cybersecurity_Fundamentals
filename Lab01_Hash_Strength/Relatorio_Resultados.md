# Relatório de Resultados

## Disciplina: Fundamentos de Segurança da Informação

## Atividade: Teste de Força Bruta com MD5

---

## 1. Objetivo

O objetivo desta atividade foi analisar o tempo necessário para encontrar uma pré-imagem de um hash MD5 utilizando o método de força bruta, considerando diferentes conjuntos de caracteres.

Foram realizados testes com:

* Apenas letras minúsculas;
* Letras minúsculas e maiúsculas;
* Todos os caracteres imprimíveis.

Cada teste foi repetido 10 vezes para cálculo do tempo médio.

---

## 2. Metodologia

Para a realização dos testes, foi desenvolvido um programa em Python que executa as seguintes etapas:

1. Seleciona aleatoriamente um caractere do conjunto escolhido;
2. Gera o hash MD5 desse caractere;
3. Percorre todo o conjunto tentando encontrar o caractere correspondente;
4. Mede o tempo gasto até encontrar a correspondência;
5. Repete o processo 10 vezes;
6. Calcula o tempo médio.

O tempo foi medido em segundos utilizando a biblioteca `time`.

---

## 3. Conjuntos de Caracteres Utilizados

| Conjunto                        | Descrição                           | Quantidade |
| ------------------------------- | ----------------------------------- | ---------- |
| Letras minúsculas               | a até z                             | 26         |
| Letras minúsculas e maiúsculas  | a até z e A até Z                   | 52         |
| Todos os caracteres imprimíveis | Letras, números, símbolos e espaços | 100        |

---

## 4. Resultados Obtidos

### 4.1 Letras Minúsculas

Total de símbolos: 26

Tempo médio: **5.1 × 10⁻⁵ segundos**

| Tentativa | Letra | Tempo (s) |
| --------- | ----- | --------- |
| 1         | p     | 0.000102  |
| 2         | l     | 0.000065  |
| 3         | a     | 0.000010  |
| 4         | h     | 0.000040  |
| 5         | b     | 0.000015  |
| 6         | g     | 0.000049  |
| 7         | b     | 0.000023  |
| 8         | s     | 0.000097  |
| 9         | n     | 0.000067  |
| 10        | h     | 0.000042  |

---

### 4.2 Letras Minúsculas e Maiúsculas

Total de símbolos: 52

Tempo médio: **1.39 × 10⁻⁴ segundos**

| Tentativa | Letra | Tempo (s) |
| --------- | ----- | --------- |
| 1         | F     | 0.000143  |
| 2         | o     | 0.000075  |
| 3         | E     | 0.000155  |
| 4         | U     | 0.000227  |
| 5         | O     | 0.000325  |
| 6         | N     | 0.000211  |
| 7         | h     | 0.000041  |
| 8         | k     | 0.000061  |
| 9         | m     | 0.000062  |
| 10        | u     | 0.000093  |

---

### 4.3 Todos os Caracteres Imprimíveis

Total de símbolos: 100

Tempo médio: **7.46 × 10⁻⁴ segundos**

| Tentativa | Letra   | Tempo (s) |
| --------- | ------- | --------- |
| 1         | [       | 0.000361  |
| 2         | (vazio) | 0.000791  |
| 3         | (vazio) | 0.000363  |
| 4         | U       | 0.004029  |
| 5         | S       | 0.000276  |
| 6         | :       | 0.000560  |
| 7         | F       | 0.000239  |
| 8         | }       | 0.000417  |
| 9         | +       | 0.000292  |
| 10        | r       | 0.000133  |

---

## 5. Análise dos Resultados

Com base nos resultados obtidos, é possível observar que:

* Quanto maior o conjunto de caracteres, maior é o tempo necessário para encontrar a correspondência;
* O conjunto com apenas letras minúsculas apresentou o menor tempo médio;
* O conjunto com todos os caracteres foi o mais demorado;
* O aumento do número de símbolos aumenta a quantidade de tentativas necessárias.

Isso ocorre porque o método de força bruta testa todas as possibilidades até encontrar a correta.

---

## 6. Conclusão

A atividade demonstrou, na prática, como o tamanho do conjunto de caracteres influencia diretamente na segurança de um sistema baseado em hash.

Quanto maior o número de possibilidades, maior é o tempo necessário para quebrar o hash, tornando o sistema mais seguro contra ataques de força bruta.

Dessa forma, recomenda-se o uso de senhas longas e com variedade de caracteres para aumentar a segurança das informações.

---

## 7. Considerações Finais

O algoritmo MD5, apesar de ser rápido, não é considerado seguro atualmente para aplicações críticas, pois apresenta vulnerabilidades conhecidas.

Mesmo assim, ele é útil para fins educacionais e para demonstração de conceitos básicos de segurança da informação.
