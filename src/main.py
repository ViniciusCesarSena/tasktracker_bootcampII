"""Aplicação de terminal para gerenciamento de tarefas pessoais."""

from datetime import datetime


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


def validar_titulo():
    """Solicita um título até que seja informado um texto não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode conter apenas espaços.")


def validar_prioridade():
    """Solicita e normaliza uma prioridade aceita pelo sistema."""
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }

    while True:
        valor = input("Prioridade (Alta, Média ou Baixa): ").strip().casefold()
        if valor in prioridades:
            return prioridades[valor]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def validar_data():
    """Solicita uma data existente e no formato exato DD/MM/AAAA."""
    while True:
        valor = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(valor, "%d/%m/%Y")
            if data.strftime("%d/%m/%Y") == valor:
                return valor
        except ValueError:
            pass
        print("Erro: informe uma data válida no formato DD/MM/AAAA.")


def solicitar_id(operacao):
    """Solicita um identificador numérico para a operação indicada."""
    valor = input(f"ID da tarefa a {operacao}: ").strip()
    try:
        return int(valor)
    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")
        return None


def cadastrar_tarefa(tarefas, proximo_id):
    """Recebe os dados e adiciona uma tarefa à lista."""
    tarefa = {
        "id": proximo_id,
        "titulo": validar_titulo(),
        "descricao": input("Descrição: ").strip(),
        "prioridade": validar_prioridade(),
        "data_limite": validar_data(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa["titulo"]}" cadastrada com sucesso!')
    return tarefa


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

    pendentes = sum(tarefa["status"] == "Pendente" for tarefa in tarefas)
    concluidas = sum(tarefa["status"] == "Concluída" for tarefa in tarefas)
    print("\n========== RESUMO ==========\n")
    print(f"Total de tarefas: {len(tarefas)}")
    print(f"Pendentes: {pendentes}")
    print(f"Concluídas: {concluidas}")


def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    identificador = solicitar_id("concluir")
    if identificador is None:
        return

    tarefa = buscar_tarefa(tarefas, identificador)
    if not tarefa:
        print("Tarefa não encontrada.")
        return

    if tarefa["status"] == "Concluída":
        print("A tarefa já está concluída. Nenhuma alteração foi realizada.")
        return

    tarefa["status"] = "Concluída"
    print("Tarefa concluída com sucesso!")


def remover_tarefa(tarefas):
    """Remove uma tarefa após confirmação."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    identificador = solicitar_id("remover")
    if identificador is None:
        return

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
    elif confirmacao == "N":
        print("Remoção cancelada.")
    else:
        print("Confirmação inválida. Remoção cancelada.")


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
