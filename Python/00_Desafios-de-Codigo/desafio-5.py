valor = float(input())

if valor > 0:
  print(f"Deposito realizado com sucesso!\nSaldo atual: R$ ", "%.2f" % round(valor, 2) )
elif valor == 0:
  print('Encerrando o programa...')
else:
  print('Valor invalido! Digite um valor maior que zero.')