# Objetivo
"""Criar uma lista de tarefas, que será feita a partir de uma interação do usuário 
e disponibilizara a possibilidade do usuário dar como concluído ou não (deletar)
e ver as tarefas que ele tem"""

titulo = () # Variável para armazenar o título da tarefa
descritivo = () # Variável para armazenar o descritivo da tarefa
tarefas = {}  # Cria um dicionário vazio para armazenar as tarefas
opcao = ()  # Variável para armazenar a opção escolhida pelo usuário

opcao1 = ["1", "adicionar", "adicionar tarefa", "1 - adicionar tarefa"]  # Lista de opções para adicionar tarefa
opcao2 = ["2", "ver", "ver tarefas", "2 - ver tarefas"]  # Lista de opções para ver tarefas
opcao3 = ["3", "deletar", "deletar tarefa", "3 - deletar tarefa"]  # Lista de opções para deletar tarefa
opcao4 = ["4", "sair", "4 - sair"]  # Lista de opções para sair

def menu():
    print("Escolha uma opção:\n"
          "1 - Adicionar tarefa\n"
          "2 - Ver tarefas\n"
          "3 - Deletar tarefa\n"
          "4 - Sair")  # Exibe o menu de opções para o usuário
    
    opcao = input("Digite sua opção:").strip().lower()  # Normaliza a entrada do usuário


# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas, titulo, descritivo): 
    titulo = input("Insira um identificador único para a tarefa (ex: Tarefa1): ").strip()
    if titulo in tarefas:
        print(f"Já existe uma tarefa com o identificador '{titulo}'. Tente novamente.")
    else:
        descritivo = input("Insira a descrição da tarefa: ").strip()
        tarefas[titulo] = descritivo  # Adiciona a tarefa ao dicionário
        print(f"Tarefa '{titulo}' adicionada com sucesso!")

# Função para visualizar as tarefas
def ver_tarefas(tarefas):
    if tarefas:
            print("Tarefas:")
            for titulo, descritivo in tarefas.items():
                print(f"{titulo}: {descritivo}")  # Exibe as tarefas com identificadores
    else:
        print("Nenhuma tarefa encontrada.")

# Função para deletar uma tarefa
def deletar_tarefa(tarefas, titulo):
    titulo = input("Insira o identificador da tarefa que deseja deletar: ").strip()
    if titulo in tarefas:  # Se a tarefa estiver no dicionário
        del tarefas[titulo]  # Remove a tarefa do dicionário
        print(f"Tarefa '{titulo}' removida com sucesso!")
    else:
        print(f"Tarefa '{titulo}' não encontrada no dicionário!")

# Função para sair do programa
def sair():
    continuar = False  # A variável continuar passa a ser False e o loop para de rodar
    print("Saindo do programa. Até mais!")

# Função para exibir mensagem de erro para opção inválida
def opcao_invalida():
    print("Opção inválida! Tente novamente.")  # Exibe mensagem de erro para opção inválida

continuar = True  # Variável de controle para o loop principal


while continuar:  # Inicia um loop que continuará até que a variável continuar seja False
    menu () # Chama a função menu para exibir as opções

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