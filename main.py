import argparse
from arquivos import gerar_cpfs, gerar_rgs, gerar_cnpjs, gerar_cpfs_n, gerar_rgs_n, gerar_cnpjs_n

# Configurar argumentos de linha de comando
parser = argparse.ArgumentParser(description="Gerar documentos (CPF, RG, CNPJ).")
parser.add_argument("--cpf", type=int, help="Número de CPFs a gerar.")
parser.add_argument("--rg", type=int, help="Número de RGs a gerar.")
parser.add_argument("--cnpj", type=int, help="Número de CNPJs a gerar.")
parser.add_argument("-n", action="store_true", help="Retirar o nome da variável da primeira linha.")
# Analisar os argumentos da linha de comando
args = parser.parse_args()

# Verificar quais geradores foram escolhidos
if args.cpf is not None:
    gerar_cpfs(args.cpf)
    if args.n:
        gerar_cpfs_n(args.cpf)

if args.rg is not None:
    gerar_rgs(args.rg)
    if args.n:
        gerar_rgs_n(args.rg)

if args.cnpj is not None:
    gerar_cnpjs(args.cnpj)
    if args.n:
        gerar_cnpjs_n(args.cnpj)

if not any(vars(args).values()):
    print("Nenhum gerador escolhido. Use os argumentos --cpf, --rg e/ou --cnpj para escolher quantos geradores deseja executar.")
