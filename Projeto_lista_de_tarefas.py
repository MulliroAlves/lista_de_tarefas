# Objetivo
"""Criar uma lista de tarefas, que será feita a partir de uma interação do usuário 
e disponibilizara a possibilidade do usuário dar como concluído ou não (deletar)
e ver as tarefas que ele tem"""

import time  # Importa o módulo time para manipulação de tempo

titulo = () # Variável para armazenar o título da tarefa
descritivo = () # Variável para armazenar o descritivo da tarefa
tarefas = {}  # Cria um dicionário vazio para armazenar as tarefas
opcao = () # Variável para armazenar a opção escolhida pelo usuário
continuar = () # Variável para controlar o loop principal


# Listas de opções para o menu
opcao1 = ["1", "adicionar", "adicionar tarefa", "1 - adicionar tarefa"]  # Lista de opções para adicionar tarefa
opcao2 = ["2", "ver", "ver tarefas", "2 - ver tarefas"]  # Lista de opções para ver tarefas
opcao3 = ["3", "deletar", "deletar tarefa", "3 - deletar tarefa"]  # Lista de opções para deletar tarefa
opcao4 = ["4", "sair", "4 - sair"]  # Lista de opções para sair

def inserir_linha():
    time.sleep (0.5)  # Pausa a execução por 1 segundo para simular processamento
    print("-" * 15, end="")
    time.sleep(1)
    print("-" * 20, end="")
    time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
    print("\n")  # Exibe uma linha em branco para melhor visualização

def menu():
    print("Escolha uma opção:\n"
          "1 - Adicionar tarefa\n"
          "2 - Ver tarefas\n"
          "3 - Deletar tarefa\n"
          "4 - Sair")  # Exibe o menu de opções para o usuário
    print ("\n") # Exibe uma linha separadora para melhor visualização)

    return input("Digite sua opção:").strip().lower()  # Normaliza a entrada do usuário


# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, titulo, descritivo): 
    titulo = input("Insira um identificador único para a tarefa (ex: Tarefa1): ").strip()
    if titulo in tarefas:
        time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
        print ("\n") , print(f"Já existe uma tarefa com o identificador '{titulo}'. Tente novamente.")
        inserir_linha()  # Chama a função para inserir uma linha separadora

    else:
        descritivo = input("Insira a descrição da tarefa: ").strip()
        tarefas[titulo] = descritivo  # Adiciona a tarefa ao dicionário
        time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
        print ("\n") , print(f"Tarefa '{titulo}' adicionada com sucesso!")
        inserir_linha ()  # Chama a função para inserir uma linha separadora
    
# Função para visualizar as tarefas
def ver_tarefas(tarefas):
    if tarefas:
            n = 1 # Inicializa o contador de tarefas
            time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
            print("\n")  # Exibe uma linha em branco para melhor visualização
            print(f" {" " * 10} {"Tarefas:"} {"\n"}")
            for titulo, descritivo in tarefas.items():
                time.sleep(0.5)  # Pausa a execução por 0.5 segundos para simular processamento
                print(f" {" " * 10} {n} - {titulo}: {descritivo}")  # Exibe as tarefas com identificadores
                n = n + 1  # Incrementa o contador de tarefas (pode ser também feito com n += 1)
                inserir_linha()  # Chama a função para inserir uma linha separadora

    else:
        time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
        print("\n")  # Exibe uma linha em branco para melhor visualização
        print("Nenhuma tarefa encontrada.")
        inserir_linha()  # Chama a função para inserir uma linha separadora
        
# Função para deletar uma tarefa
def deletar_tarefa(tarefas, titulo):
    time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
    titulo = input("Insira o identificador da tarefa que deseja deletar: ").strip()
    if titulo in tarefas:  # Se a tarefa estiver no dicionário
        del tarefas[titulo]  # Remove a tarefa do dicionário
        time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
        print("\n")  # Exibe uma linha em branco para melhor visualização
        print(f"Tarefa '{titulo}' removida com sucesso!")
        inserir_linha()  # Chama a função para inserir uma linha separadora

        ver_tarefas(tarefas)  # Chama a função para exibir as tarefas restantes

    else:
        time.sleep(1)  # Se a tarefa não estiver no dicionário, exibe mensagem de erro
        print("\n")  # Exibe uma linha em branco para melhor visualização
        print(f"Tarefa '{titulo}' não encontrada no dicionário!")
        inserir_linha()  # Chama a função para inserir uma linha separadora

# Função para sair do programa
def sair():
    global continuar  # Declara que estamos usando a variável global 'continuar'
    continuar = False  # Define 'continuar' como False para encerrar o loop
    time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
    print("\n")  # Exibe uma linha em branco para melhor visualização
    print("Saindo do programa. Até mais!")

# Função para exibir mensagem de erro para opção inválida
def opcao_invalida():
    time.sleep(1)  # Pausa a execução por 1 segundo para simular processamento
    print("Opção inválida! Tente novamente.")  # Exibe mensagem de erro para opção inválida
    inserir_linha()  # Chama a função para inserir uma linha separadora


continuar = True  # Variável para controlar o loop principal
print("\n")  # Exibe uma linha em branco para melhor visualização
print("Bem-vinde a lista de tarefas!")  # Mensagem de boas-vindas
inserir_linha()  # Chama a função para inserir uma linha separadora

while continuar:  # Inicia um loop que continuará até que a variável continuar seja False
    opcao = menu () # Chama a função menu para exibir as opções

    if opcao in opcao1:  # Se a opção for 1, adiciona uma nova tarefa
        adicionar_tarefa(tarefas, titulo, descritivo)  # Chama a função para adicionar tarefa

    elif opcao in opcao2:  # Se a opção for 2, exibe as tarefas
        ver_tarefas(tarefas)
       
    elif opcao in opcao3:  # Se a opção for 3, deleta uma tarefa
        deletar_tarefa(tarefas, titulo)

    elif opcao in opcao4:  # Se a opção for 4, sai do programa
        sair()

    else:  # Se a opção não for válida, exibe mensagem de erro
       opcao_invalida()

print("Programa encerrado.")
