
# import csv

# def ler_csv(arquivo):
#     with open(arquivo, 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter='|')
#         for i, row in enumerate(reader, start=1):
#             print(f"{i}. {row['questions']}")

# def adicionar_objeto(arquivo, novo_topico):
#     tópicos_validos = [
#         "Introducao",
#         "Assembly",
#         "Monociclo",
#         "Pipeline",
#         "Hierarquia",
#         "ES",
#         "Barramento"
#     ]
#     if novo_topico not in tópicos_validos:
#         print("Tópico inválido. Por favor, escolha um dos seguintes tópicos:")
#         for tópico in tópicos_validos:
#             print(f"- {tópico}")
#         return
    
#     nova_pergunta = []
#     nova_resposta = []
    
#     print("Digite a pergunta (digite '##fim##' em uma linha separada para terminar):")
#     while True:
#         linha = input()
#         if linha == "##fim##":
#             break
#         nova_pergunta.append(linha)
    
#     print("Digite a resposta (digite '##fim##' em uma linha separada para terminar):")
#     while True:
#         linha = input()
#         if linha == "##fim##":
#             break
#         nova_resposta.append(linha)
    
#     nova_pergunta = '\n'.join(nova_pergunta)
#     nova_resposta = '\n'.join(nova_resposta)
    
#     novo_objeto = [novo_topico, nova_pergunta, nova_resposta]
#     with open(arquivo, 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter='|')
#         writer.writerow(novo_objeto)

# def excluir_objeto(arquivo, numero_questao):
#     linhas = []
#     with open(arquivo, 'r', newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter='|')
#         header = next(reader)  # Ler o cabeçalho e armazená-lo
#         linhas.append(header)  # Adicionar o cabeçalho à lista de linhas
#         for i, row in enumerate(reader, start=1):
#             if i != numero_questao:
#                 linhas.append(row)

#     with open(arquivo, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter='|')
#         writer.writerows(linhas)

# # Nome do arquivo CSV
# arquivo_csv = 'in.csv'

# # Ler o arquivo CSV
# ler_csv(arquivo_csv)

# # Opção de adicionar ou excluir objeto
# opcao = input("Deseja adicionar (a) ou excluir (e) um objeto? ")

# if opcao.lower() == 'a':
#     # Obter o novo tópico
#     novo_topico = input("Novo tópico: ")
    
#     # Adicionar um novo objeto ao arquivo
#     adicionar_objeto(arquivo_csv, novo_topico)
# elif opcao.lower() == 'e':
#     # Obter o número da questão a ser excluída
#     numero_questao = int(input("Número da questão a ser excluída: "))
    
#     # Excluir o objeto do arquivo
#     excluir_objeto(arquivo_csv, numero_questao)
# else:
#     print("Opção inválida!")

# # Ler o arquivo novamente para verificar as alterações
# ler_csv(arquivo_csv)

import csv
import shutil

def fazer_copia_arquivo(origem, destino):
    shutil.copyfile(origem, destino)

def ler_csv(arquivo):
    with open(arquivo, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row['questions']}")

def adicionar_objeto(arquivo, novo_topico):
    tópicos_validos = [
        "Introducao",
        "Assembly",
        "Monociclo",
        "Pipeline",
        "Hierarquia",
        "ES",
        "Barramento"
    ]
    if novo_topico not in tópicos_validos:
        print("Tópico inválido. Por favor, escolha um dos seguintes tópicos:")
        for tópico in tópicos_validos:
            print(f"- {tópico}")
        return
    
    nova_pergunta = []
    nova_resposta = []
    
    print("Digite a pergunta (digite '##fim##' em uma linha separada para terminar):")
    while True:
        linha = input()
        if linha == "##fim##":
            break
        nova_pergunta.append(linha)
    
    print("Digite a resposta (digite '##fim##' em uma linha separada para terminar):")
    while True:
        linha = input()
        if linha == "##fim##":
            break
        nova_resposta.append(linha)
    
    nova_pergunta = '\n'.join(nova_pergunta)
    nova_resposta = '\n'.join(nova_resposta)
    
    novo_objeto = [novo_topico, nova_pergunta, nova_resposta]
    with open(arquivo, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(novo_objeto)

def excluir_objeto(arquivo, numero_questao):
    linhas = []
    with open(arquivo, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        header = next(reader)  # Ler o cabeçalho e armazená-lo
        linhas.append(header)  # Adicionar o cabeçalho à lista de linhas
        for i, row in enumerate(reader, start=1):
            if i != numero_questao:
                linhas.append(row)

    with open(arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(linhas)

# Nome do arquivo CSV
arquivo_csv = 'in.csv'

# Criar uma cópia do arquivo antes de qualquer mudança
arquivo_copia = 'in_copia.csv'
fazer_copia_arquivo(arquivo_csv, arquivo_copia)

# Ler o arquivo CSV
ler_csv(arquivo_csv)

# Opção de adicionar ou excluir objeto
opcao = input("Deseja adicionar (a) ou excluir (e) um objeto? ")

if opcao.lower() == 'a':
    # Obter o novo tópico
    novo_topico = input("Novo tópico: ")
    
    # Adicionar um novo objeto ao arquivo
    adicionar_objeto(arquivo_csv, novo_topico)
elif opcao.lower() == 'e':
    # Obter o número da questão a ser excluída
    numero_questao = int(input("Número da questão a ser excluída: "))
    
    # Excluir o objeto do arquivo
    excluir_objeto(arquivo_csv, numero_questao)
else:
    print("Opção inválida!")

# Ler o arquivo novamente para verificar as alterações
ler_csv(arquivo_csv)
