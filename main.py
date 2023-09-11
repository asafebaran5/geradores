from geradores import geraCPF, geraRG

# Cria o arquivo "cpf.txt" e abre para escrita
with open("cpf.txt", "w") as arquivo:
  for i in range(1000):
    cpf = geraCPF()
    arquivo.write(cpf + "\n")

print("Arquivo 'cpf.txt' criado e CPFs gerados e salvos nele.")

# Cria o arquivo "rg.txt" e abre para escrita
with open("rg.txt", "w") as arquivo:
  for i in range(1000):
    rg = geraRG()
    arquivo.write(rg + "\n")

print("Arquivo 'rg.txt' criado e RGs gerados e salvos nele.")