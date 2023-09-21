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
    def calcula_digito_verificador(rg_parcial):
        soma = 0
        for i, valor in enumerate(rg_parcial):
            soma += int(valor) * (10 - i)
        digito = 11 - (soma % 11)
        return digito if digito <= 9 else 0

    rg_base = [random.randint(0, 9) for _ in range(8)]
    digito1 = calcula_digito_verificador(rg_base)
    rg_base.append(digito1)
    digito2 = calcula_digito_verificador(rg_base)
    rg_base.append(digito2)

    return ''.join(map(str, rg_base))


def geraCNPJ():
    def calcula_digito_verificador(cnpj_parcial):
        if len(cnpj_parcial) == 12:
            multiplicadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        else:
            multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        soma = sum(int(c) * m for c, m in zip(cnpj_parcial, multiplicadores))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    cnpj_base = [random.randint(0, 9) for _ in range(12)]
    digito1 = calcula_digito_verificador(cnpj_base)
    cnpj_base.append(digito1)
    digito2 = calcula_digito_verificador(cnpj_base)
    cnpj_base.append(digito2)

    return ''.join(map(str, cnpj_base))
