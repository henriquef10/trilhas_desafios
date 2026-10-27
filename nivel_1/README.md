# PDV — Ponto de Venda

## O que o código faz

O projeto é um sistema simples de Ponto de Venda (PDV) desenvolvido em Python. O programa permite registrar compras e calcular descontos com base na idade do cliente, no valor da compra, na quantidade de itens e na utilização de um cupom de desconto. Ao finalizar, exibe o histórico das compras, calcula os totais e gera um arquivo resumo.txt com o resumo das operações realizadas.

## Como ele faz

1. Entrada de dados: solicita o valor da compra, a idade do cliente, a quantidade de itens e um cupom de desconto, caso exista.

2. Validação: verifica se o valor da compra é negativo ou se a idade e a quantidade de itens são menores ou iguais a zero. Caso algum dado seja inválido, solicita uma nova entrada.

3. Desconto por idade: se o cliente tiver 65 anos ou mais, aplica 20% de desconto sobre o valor da compra.

4. Desconto por valor: se o valor da compra, após o desconto anterior, for maior que R$ 100,00, aplica mais 10% de desconto.

5. Desconto por quantidade: se a compra possuir mais de 3 itens, aplica 5% de desconto sobre o valor restante.

6. Desconto por cupom: se o cliente informar o cupom FIDELIDADE10, aplica mais 10% de desconto sobre o valor restante.

7. Cálculo do valor final: subtrai todos os descontos concedidos do valor original da compra.

8. Registro da compra: armazena as informações em uma lista chamada historicoCompras.

9. Finalização: o processo se repete até que o usuário informe 0 como valor da compra.

10. Resumo: ao finalizar, percorre o histórico e calcula o total de compras realizadas, os descontos concedidos, o valor bruto e o valor final.

11. Gravação em arquivo: salva o resumo no arquivo resumo.txt e exibe as informações no terminal.

Importante: os descontos são aplicados sucessivamente. Isso significa que cada novo desconto é calculado sobre o valor restante após a aplicação dos descontos anteriores, e não diretamente sobre o valor original da compra.

## Como rodar

É necessário ter o **Python 3** instalado. No terminal, abra a pasta onde está o arquivo `pdv.py` e execute:

```bash
python pdv.py
```

O programa solicitará as informações de cada compra:

Digite o valor da compra: 200
Digite a idade do cliente: 65
Digite a quantidade de itens: 4
Digite o cupom de desconto: FIDELIDADE10

Resultado:

Valor final esperado: R$ 123.12

Para registrar outras compras, basta continuar informando os valores solicitados.

Para encerrar, digite `0` quando o programa solicitar o valor de uma nova compra.

## Tabela de exemplos

| # | Valor R$ | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---:|---|---:|---:|
| 1 | R$ 50,00 | 30 | 0% | 0% | R$ 50,00 |
| 2 | R$ 100,00 | 30 | 0% | 0% | R$ 100,00 |
| 3 | R$ 80,00 | 65 | 20% | 0% | R$ 64,00 |
| 4 | R$ 100,00 | 70 | 20% | 0% | R$ 80,00 |
| 5 | R$ 125,00 | 70 | 20% | 0% | R$ 100,00 |
| 6 | R$ 200,00 | 30 | 0% | 10% | R$ 180,00 |
| 7 | R$ 101,00 | 30 | 0% | 10% | R$ 90,90 |
| 8 | R$ 200,00 | 65 | 20% | 10% | R$ 144,00 |
| 9 | R$ 1000,00 | 80 | 20% | 10% | R$ 720,00 |
| 10 | R$ 200,00 | 64 | 0% | 10% | R$ 180,00 |

**Outros casos:** digitar `0` como valor da compra encerra o programa; informar compra, ou idade, ou quantidade negativa faz o programa rejeitar a entrada e pedir novamente.
