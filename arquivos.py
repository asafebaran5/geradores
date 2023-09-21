import os
from geradores import geraCPF, geraRG, geraCNPJ

# Função para gerar CPFs
def gerar_cpfs(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "cpf.txt"), "w") as arquivo:
        for _ in range(quantidade):
            cpf = geraCPF()
            arquivo.write(cpf + "\n")
    print(f"{quantidade} CPFs gerados e salvos em 'massas/cpf.txt'.")

# Função para gerar RGs
def gerar_rgs(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "rg.txt"), "w") as arquivo:
        for _ in range(quantidade):
            rg = geraRG()
            arquivo.write(rg + "\n")
    print(f"{quantidade} RGs gerados e salvos em 'massas/rg.txt'.")

# Função para gerar CNPJs
def gerar_cnpjs(quantidade):
    pasta = "massas"
    os.makedirs(pasta, exist_ok=True)  # Cria o diretório "massas" se não existir
    with open(os.path.join(pasta, "cnpj.txt"), "w") as arquivo:
        for _ in range(quantidade):
            cnpj = geraCNPJ()
            arquivo.write(cnpj + "\n")
    print(f"{quantidade} CNPJs gerados e salvos em 'massas/cnpj.txt'.")
