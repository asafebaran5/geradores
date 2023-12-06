import os
import argparse
from geradores import geraCPF, geraRG, geraCNPJ

# Função para gerar CPFs
def gerar_cpfs(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "cpf.txt"), "w") as arquivo:
        arquivo.write('cpf' + '\n')
        for i in range(quantidade):
            cpf = geraCPF()
            if i == quantidade - 1:
                arquivo.write(cpf)  # Para a última linha, não inclui o caractere de quebra de linha
            else:
                arquivo.write(cpf + "\n")
    print(f"{quantidade} CPFs gerados e salvos em 'massas/cpf.txt'.")

# Função para gerar RGs
def gerar_rgs(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "rg.txt"), "w") as arquivo:
        arquivo.write('rg' + '\n')
        for i in range(quantidade):
            rg = geraRG()
            if i == quantidade - 1:
                arquivo.write(rg)  # Para a última linha, não inclui o caractere de quebra de linha
            else:
                arquivo.write(rg + "\n")
    print(f"{quantidade} RGs gerados e salvos em 'massas/rg.txt'.")

# Função para gerar CNPJs
def gerar_cnpjs(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "cnpj.txt"), "w") as arquivo:
        arquivo.write('cnpj' + '\n')
        for i in range(quantidade):
            cnpj = geraCNPJ()
            if i == quantidade - 1:
                arquivo.write(cnpj)  # Para a última linha, não inclui o caractere de quebra de linha
            else:
                arquivo.write(cnpj + "\n")
    print(f"{quantidade} CNPJs gerados e salvos em 'massas/cnpj.txt'.")



# Função para gerar CPFs sem o nome da variável
def gerar_cpfs_n(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "cpf.txt"), "w") as arquivo:
        for i in range(quantidade):
            cpf = geraCPF()
            if i == quantidade - 1:
                arquivo.write(cpf)  # Para a última linha, não inclui o caractere de quebra de linha
            else:
                arquivo.write(cpf + "\n")

# Função para gerar RGs sem o nome da variável
def gerar_rgs_n(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "rg.txt"), "w") as arquivo:
        for i in range(quantidade):
            rg = geraRG()
            if i == quantidade - 1:
                arquivo.write(rg)  # Para a última linha, não inclui o caractere de quebra de linha
            else:
                arquivo.write(rg + "\n")

# Função para gerar CNPJs sem o nome da variável
def gerar_cnpjs_n(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "cnpj.txt"), "w") as arquivo:
        for i in range(quantidade):
            cnpj = geraCNPJ()
            if i == quantidade - 1:
                arquivo.write(cnpj)  # Para a última linha, não inclui o caractere de quebra de linha
            else:
                arquivo.write(cnpj + "\n")