# Gerador de CPFs, RGs e CNPJs Aleatórios

Este é um projeto em Python que gera números de CPFs, RGs e CNPJs aleatórios e os salva em arquivos de texto, para serem utilizados em massas de teste.

## Tabela de Conteúdos

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuições](#contribuições)

## Requisitos

Antes de executar este projeto, certifique-se de que você tem [Python](https://www.python.org/downloads/) instalado em seu sistema.

## Instalação

1. Clone o repositório para o seu sistema local:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git

2. Navegue até o diretório do projeto:

    ```bash
    cd seu-projeto

## Uso

### Gerar CPFs

1. Execute o script principal main.py com o seguinte sufixo:

    ```bash
    python main.py --cpf 1000

Isso gerará 1000 números de CPFs em um arquivo chamado `cpf.txt` no diretório `massas`.

> **Alerta:** em alguns casos, pode ser necessário usar `python3` em vez de `python` para chamar o interpretador Python 3 no Linux.

### Gerar RGs

1. Execute o script principal main.py com o seguinte sufixo:

    ```bash
    python main.py --rg 1000

Isso gerará 1000 números de RGs em um arquivo chamado `rg.txt` no diretório `massas`.

### Gerar CNPJs

1. Execute o script principal main.py com o seguinte sufixo:

    ```bash
    python main.py --cnpj 1000

Isso gerará 1000 números de CNPJs
 em um arquivo chamado `cnpj.txt` no diretório `massas`.

 ### Gerar todos os documentos

1. Execute o script principal main.py com o seguinte sufixo:

    ```bash
    python main.py --cpf 1000 --rg 1000 --cnpj 1000

Isso gerará 1000 números de CPFs, RGs e CNPJs 
no diretório `massas`, cada um com seu arquivo correspondente.

> **Lembre-se:** Caso queira gerar somente CPFs e RGs não é obrigatório colocar todos os argumentos você pode seleciona-los de acordo com sua vontade, isso é válido para todos os documentos

 ### Retirar o nome da variável da primeira linha

Caso queira que seus arquivos de massa não contenham o nome da variável (cpf, rg ou cnpj) na primeira linha adicione o argumento `-n`

1. Execute o script principal main.py com o seguinte sufixo:

    ```bash
    python main.py --cpf 1000 --rg 1000 --cnpj 1000 -n

Isso gerará 1000 números de CNPJs
 em um arquivo chamado `cnpj.txt` no diretório `massas`.

> **Lembre-se:** O argumento `-n` é valido para qualquer comando.

> **Alerta:** em alguns casos, pode ser necessário usar `python3` em vez de `python` para chamar o interpretador Python 3 no Linux.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar este projeto.


Este projeto foi criado por [Asafe Baran](https://github.com/asafebaran5).
