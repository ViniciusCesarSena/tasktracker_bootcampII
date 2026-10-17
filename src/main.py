"""Aplicação de terminal para gerenciamento de tarefas pessoais."""


def exibir_menu():
    """Exibe as opções disponíveis no TaskTracker."""
    print("\n========== TASKTRACKER ==========\n")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


def buscar_tarefa(tarefas, identificador):
    """Retorna a tarefa correspondente ao identificador informado."""
    for tarefa in tarefas:
        if tarefa["id"] == identificador:
            return tarefa
    return None


def cadastrar_tarefa(tarefas, proximo_id):
    """Recebe os dados e adiciona uma tarefa à lista."""
    tarefa = {
        "id": proximo_id,
        "titulo": input("Título: ").strip(),
        "descricao": input("Descrição: ").strip(),
        "prioridade": input("Prioridade (Alta, Média ou Baixa): ").strip(),
        "data_limite": input("Data limite (DD/MM/AAAA): ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa["titulo"]}" cadastrada com sucesso!')


def listar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    print("\n========== TAREFAS ==========")
    for tarefa in tarefas:
        print(f'\nID: {tarefa["id"]}')
        print(f'Título: {tarefa["titulo"]}')
        print(f'Descrição: {tarefa["descricao"]}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Data limite: {tarefa["data_limite"]}')
        print(f'Status: {tarefa["status"]}')


def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída."""
    identificador = int(input("ID da tarefa a concluir: "))
    tarefa = buscar_tarefa(tarefas, identificador)
    if tarefa:
        tarefa["status"] = "Concluída"
        print("Tarefa concluída com sucesso!")
    else:
        print("Tarefa não encontrada.")


def remover_tarefa(tarefas):
    """Remove uma tarefa após confirmação."""
    identificador = int(input("ID da tarefa a remover: "))
    tarefa = buscar_tarefa(tarefas, identificador)
    if not tarefa:
        print("Tarefa não encontrada.")
        return

    confirmacao = input(
        f'Remover a tarefa "{tarefa["titulo"]}"? (S/N): '
    ).strip().upper()
    if confirmacao == "S":
        tarefas.remove(tarefa)
        print("Tarefa removida com sucesso!")
    else:
        print("Remoção cancelada.")


def main():
    """Executa o menu principal até que o usuário escolha sair."""
    tarefas = []
    proximo_id = 1

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas, proximo_id)
            proximo_id += 1
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("TaskTracker encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


if __name__ == "__main__":
    main()
