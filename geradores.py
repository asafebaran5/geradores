import random


def geraCPF():
  cpf = [random.randint(0, 9) for _ in range(9)]

  # Cálculo do primeiro dígito verificador
  soma1 = sum((valor * (10 - indice)) for indice, valor in enumerate(cpf))
  digito1 = 11 - (soma1 % 11)
  cpf.append(0 if digito1 >= 10 else digito1)

  # Cálculo do segundo dígito verificador
  soma2 = sum((valor * (11 - indice)) for indice, valor in enumerate(cpf))
  digito2 = 11 - (soma2 % 11)
  cpf.append(0 if digito2 >= 10 else digito2)

  return ''.join(map(str, cpf))


def geraRG():
  rg = [random.randint(0, 9) for _ in range(8)]

  # Cálculo do primeiro dígito verificador
  soma1 = sum((valor * (10 - indice)) for indice, valor in enumerate(rg))
  digito1 = 11 - (soma1 % 11)

  # Cálculo do segundo dígito verificador
  rg_com_digito1 = rg + [digito1]
  soma2 = sum(
      (valor * (11 - indice)) for indice, valor in enumerate(rg_com_digito1))
  digito2 = 11 - (soma2 % 11)

  # Formatar o RG como uma string
  rg_str = ''.join(map(str, rg)) + str(digito1) + str(digito2)

  return rg_str
