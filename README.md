# .ibank - Sistema Bancário Simples

Este é um projeto simples, desenvolvido em Python utilizando apenas bibliotecas padrão, para simular operações bancárias básicas como **depósito**, **saque** e **extrato**. O sistema também impõe limites de saque e de transações diárias, tornando-o mais realista.

## Funcionalidades

- **Depósito**: Permite adicionar saldo à conta.
- **Saque**: Limita o saque a R$500 por transação e no máximo 3 saques diários.
- **Extrato**: Mostra o saldo disponível e o histórico de transações (depósitos e saques).

## Regras do Sistema

- O **saque** possui um **limite máximo de R$500 por operação**.
- São permitidos até **3 saques por dia**.
- Depósitos não possuem limite de valor.

## Como Usar

Clone o Repositório

```bash
git clone https://github.com/seuusuario/seu-repositorio.git
```

e execute o arquivo app.py

```bash
python app.py
```