"""Testes automatizados das regras e dos fluxos do TaskTracker."""

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import call, patch


CAMINHO_MAIN = Path(__file__).resolve().parents[1] / "src" / "main.py"
ESPECIFICACAO = importlib.util.spec_from_file_location("tasktracker", CAMINHO_MAIN)
tasktracker = importlib.util.module_from_spec(ESPECIFICACAO)
ESPECIFICACAO.loader.exec_module(tasktracker)


def tarefa_exemplo(identificador=1, status="Pendente"):
    """Cria uma tarefa válida para uso nos testes."""
    return {
        "id": identificador,
        "titulo": "Estudar Python",
        "descricao": "Revisar funções e listas",
        "prioridade": "Alta",
        "data_limite": "20/10/2026",
        "status": status,
    }


class TestTaskTracker(unittest.TestCase):
    """Verifica os 18 cenários solicitados para a Fase 2."""

    @patch("builtins.print")
    def test_01_menu_inicial(self, mock_print):
        tasktracker.exibir_menu()
        textos = " ".join(str(chamada) for chamada in mock_print.call_args_list)
        self.assertIn("TASKTRACKER", textos)
        self.assertIn("5. Sair", textos)

    @patch("builtins.input", side_effect=[
        "Estudar Python", "Revisar funções", "Alta", "20/10/2026"
    ])
    @patch("builtins.print")
    def test_02_cadastro_valido(self, _mock_print, _mock_input):
        tarefas = []
        tarefa = tasktracker.cadastrar_tarefa(tarefas, 1)
        self.assertEqual(tarefa["status"], "Pendente")
        self.assertEqual(tarefas, [tarefa])

    @patch("builtins.input", side_effect=["", "Título válido"])
    @patch("builtins.print")
    def test_03_titulo_vazio(self, mock_print, _mock_input):
        self.assertEqual(tasktracker.validar_titulo(), "Título válido")
        self.assertTrue(mock_print.called)

    @patch("builtins.input", side_effect=["   ", "  Tarefa limpa  "])
    @patch("builtins.print")
    def test_04_titulo_apenas_espacos(self, _mock_print, _mock_input):
        self.assertEqual(tasktracker.validar_titulo(), "Tarefa limpa")

    @patch("builtins.input", side_effect=["Urgente", "Baixa"])
    @patch("builtins.print")
    def test_05_prioridade_invalida(self, mock_print, _mock_input):
        self.assertEqual(tasktracker.validar_prioridade(), "Baixa")
        self.assertTrue(mock_print.called)

    @patch("builtins.input", return_value="Media")
    def test_06_prioridade_media_sem_acento(self, _mock_input):
        self.assertEqual(tasktracker.validar_prioridade(), "Média")

    @patch("builtins.input", side_effect=["2026-10-20", "20/10/2026"])
    @patch("builtins.print")
    def test_07_formato_de_data_invalido(self, mock_print, _mock_input):
        self.assertEqual(tasktracker.validar_data(), "20/10/2026")
        self.assertTrue(mock_print.called)

    @patch("builtins.input", side_effect=["31/02/2026", "28/02/2026"])
    @patch("builtins.print")
    def test_08_data_inexistente(self, _mock_print, _mock_input):
        self.assertEqual(tasktracker.validar_data(), "28/02/2026")

    @patch("builtins.print")
    def test_09_listagem_vazia(self, mock_print):
        tasktracker.listar_tarefas([])
        mock_print.assert_called_once_with("Nenhuma tarefa cadastrada no momento.")

    @patch("builtins.print")
    def test_10_listagem_preenchida_e_resumo(self, mock_print):
        tarefas = [tarefa_exemplo(), tarefa_exemplo(2, "Concluída")]
        tasktracker.listar_tarefas(tarefas)
        self.assertIn(call("Total de tarefas: 2"), mock_print.call_args_list)
        self.assertIn(call("Pendentes: 1"), mock_print.call_args_list)
        self.assertIn(call("Concluídas: 1"), mock_print.call_args_list)

    @patch("builtins.input", side_effect=[
        "Primeira", "Descrição", "Alta", "01/11/2026",
        "Segunda", "Descrição", "Baixa", "02/11/2026",
    ])
    @patch("builtins.print")
    def test_11_ids_unicos_sem_reutilizacao(self, _mock_print, _mock_input):
        tarefas = []
        tasktracker.cadastrar_tarefa(tarefas, 1)
        tarefas.pop()
        tasktracker.cadastrar_tarefa(tarefas, 2)
        self.assertEqual(tarefas[0]["id"], 2)

    @patch("builtins.input", return_value="1")
    @patch("builtins.print")
    def test_12_concluir_tarefa_existente(self, _mock_print, _mock_input):
        tarefas = [tarefa_exemplo()]
        tasktracker.concluir_tarefa(tarefas)
        self.assertEqual(tarefas[0]["status"], "Concluída")

    @patch("builtins.input", return_value="99")
    @patch("builtins.print")
    def test_13_concluir_tarefa_inexistente(self, mock_print, _mock_input):
        tasktracker.concluir_tarefa([tarefa_exemplo()])
        mock_print.assert_called_with("Tarefa não encontrada.")

    @patch("builtins.input", return_value="1")
    @patch("builtins.print")
    def test_14_impedir_conclusao_repetida(self, mock_print, _mock_input):
        tarefas = [tarefa_exemplo(status="Concluída")]
        tasktracker.concluir_tarefa(tarefas)
        self.assertIn("já está concluída", mock_print.call_args.args[0])

    @patch("builtins.input", side_effect=["1", "S"])
    @patch("builtins.print")
    def test_15_remocao_confirmada(self, _mock_print, _mock_input):
        tarefas = [tarefa_exemplo()]
        tasktracker.remover_tarefa(tarefas)
        self.assertEqual(tarefas, [])

    @patch("builtins.input", side_effect=["1", "N"])
    @patch("builtins.print")
    def test_16_remocao_cancelada(self, _mock_print, _mock_input):
        tarefas = [tarefa_exemplo()]
        tasktracker.remover_tarefa(tarefas)
        self.assertEqual(len(tarefas), 1)

    @patch("builtins.input", side_effect=["9", "5"])
    @patch("builtins.print")
    def test_17_opcao_invalida_reexibe_menu(self, mock_print, _mock_input):
        tasktracker.main()
        mensagens = [chamada.args[0] for chamada in mock_print.call_args_list]
        self.assertIn("Opção inválida. Escolha uma opção de 1 a 5.", mensagens)
        self.assertEqual(mensagens.count("\n========== TASKTRACKER ==========\n"), 2)

    @patch("builtins.input", return_value="5")
    @patch("builtins.print")
    def test_18_saida_normal(self, mock_print, _mock_input):
        tasktracker.main()
        mock_print.assert_called_with("TaskTracker encerrado. Até logo!")


if __name__ == "__main__":
    unittest.main()
