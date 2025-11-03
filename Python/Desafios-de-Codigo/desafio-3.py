# Entrada de dados
saldo_total = 1000
valor_saque = 2000

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.


def saque(saldo_total, valor_saque):
    if saldo_total >= valor_saque:
      saldo = saldo_total - valor_saque
      print(f"Saque realizado com sucesso! Novo saldo: {saldo}")
      return saldo
    else:
        saldo = saldo_total
        print("Saldo insuficiente. Saque nao realizado!")
        return saldo

novo_saldo = saque(saldo_total, valor_saque)

saldo_total = novo_saldo
print(novo_saldo)