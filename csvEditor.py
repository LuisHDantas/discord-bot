# import csv

# def ler_csv(arquivo):
#     with open(arquivo, 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter='|')
#         for row in reader:
#             print(row)

# def adicionar_objeto(arquivo, novo_topico, nova_pergunta, nova_resposta):
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
    
#     novo_objeto = [novo_topico, nova_pergunta, nova_resposta]
#     with open(arquivo, 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter='|')
#         writer.writerow(novo_objeto)

# # Nome do arquivo CSV
# arquivo_csv = 'in.csv'

# # Ler o arquivo CSV
# ler_csv(arquivo_csv)

# # Obter as informações do novo objeto
# novo_topico = input("Novo tópico: ")
# nova_pergunta = input("Nova pergunta: ")
# nova_resposta = input("Nova resposta: ")

# # Adicionar um novo objeto ao arquivo
# adicionar_objeto(arquivo_csv, novo_topico, nova_pergunta, nova_resposta)

# # Ler o arquivo novamente para verificar a adição do novo objeto
# ler_csv(arquivo_csv)

import csv

def ler_csv(arquivo):
    with open(arquivo, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row['questions']}")

def adicionar_objeto(arquivo, novo_topico, nova_pergunta, nova_resposta):
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

# Ler o arquivo CSV
ler_csv(arquivo_csv)

# Opção de adicionar ou excluir objeto
opcao = input("Deseja adicionar (a) ou excluir (e) um objeto? ")

if opcao.lower() == 'a':
    # Obter as informações do novo objeto
    novo_topico = input("Novo tópico: ")
    nova_pergunta = input("Nova pergunta: ")
    nova_resposta = input("Nova resposta: ")
    
    # Adicionar um novo objeto ao arquivo
    adicionar_objeto(arquivo_csv, novo_topico, nova_pergunta, nova_resposta)
elif opcao.lower() == 'e':
    # Obter o número da questão a ser excluída
    numero_questao = int(input("Número da questão a ser excluída: "))
    
    # Excluir o objeto do arquivo
    excluir_objeto(arquivo_csv, numero_questao)
else:
    print("Opção inválida!")

# Ler o arquivo novamente para verificar as alterações
ler_csv(arquivo_csv)
