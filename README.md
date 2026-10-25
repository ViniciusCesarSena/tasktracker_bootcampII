# TaskTracker

Gerenciador de tarefas pessoais executado no terminal, desenvolvido em Python
ao longo das três fases do Bootcamp II. A aplicação transforma o planejamento
lógico da Fase 1 em um programa funcional, agora empacotado para execução
reprodutível com Docker, com dados mantidos temporariamente em memória.

## Objetivo

O TaskTracker reúne tarefas que poderiam ficar dispersas em anotações ou na
memória. Ele permite registrar prazos e prioridades, acompanhar o andamento das
atividades e reduzir o risco de esquecer compromissos.

## Funcionalidades

- cadastrar tarefas com título, descrição, prioridade e data limite;
- visualizar todas as propriedades de cada tarefa;
- mostrar um resumo de tarefas pendentes e concluídas;
- concluir uma tarefa pendente por meio de seu ID;
- remover uma tarefa por ID após confirmação;
- manter o menu ativo após entradas inválidas;
- gerar IDs únicos sem reutilizá-los durante a execução.

Os dados existem somente enquanto o programa está aberto. Esta etapa não usa
banco de dados, interface gráfica ou serviços externos.

## Tecnologias utilizadas

- Python 3;
- módulos `datetime` e `unittest` da biblioteca padrão;
- Docker e Docker Compose para containerização e execução interativa;
- Git para controle de versão;
- Markdown para documentação.

Não há dependências Python externas.

## Estrutura do repositório

```text
tasktracker-projeto/
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── docs/
│   ├── planejamento_logico.pdf
│   ├── roteiro_apresentacao.md
│   └── roteiro_fase3.md
├── src/
│   └── main.py
└── tests/
    └── test_main.py
```

## Pré-requisitos

- Python 3.10 ou mais recente instalado;
- Docker com o plugin Docker Compose, para a execução em contêiner;
- terminal compatível com UTF-8;
- Git, necessário apenas para versionamento e publicação.

Confirme a instalação com `python --version`. Em algumas distribuições Linux ou
instalações do Windows, o comando disponível pode ser `python3` ou `py`.

## Execução

No Windows, abra o PowerShell ou Prompt de Comando na raiz do projeto:

```powershell
python src/main.py
```

No Linux ou macOS, abra o terminal na raiz do projeto:

```bash
python3 src/main.py
```

O comando principal solicitado para o projeto é:

```bash
python src/main.py
```

## Execução com Docker

Na raiz do repositório, execute os comandos abaixo. Eles estão prontos para
copiar e colar:

```bash
docker build -t tasktracker .
docker run -it --rm tasktracker
docker compose run --rm tasktracker
```

O `Dockerfile` é a receita usada para construir a imagem da aplicação. A imagem
base `python:3.11-slim` fornece o Python 3.11 em uma distribuição reduzida, o que
mantém a imagem leve e suficiente para este projeto sem dependências externas.
`PYTHONUNBUFFERED=1` faz com que as mensagens do programa sejam enviadas
imediatamente ao terminal, sem ficarem retidas em buffer.

Como o TaskTracker usa `input()`, ele precisa de um terminal interativo para
receber as opções do menu e os dados das tarefas. No comando `docker run`, a
opção `-i` mantém a entrada padrão aberta e `-t` aloca um terminal. No Compose,
`stdin_open: true` cumpre o papel de `-i`, enquanto `tty: true` cumpre o papel de
`-t`.

Para encerrar normalmente, escolha a opção `5` no menu. O parâmetro `--rm`
remove automaticamente o contêiner encerrado, sem remover a imagem
`tasktracker`.

`docker run -it --rm tasktracker` executa diretamente uma imagem já construída.
Já `docker compose run --rm tasktracker` usa a definição do serviço
`tasktracker` em `docker-compose.yml`, centralizando o build e as configurações
de interatividade. O Compose constrói a imagem do serviço quando necessário;
`docker compose build` também pode ser usado para fazer esse build de forma
explícita.

## Exemplo de utilização

```text
========== TASKTRACKER ==========

1. Cadastrar nova tarefa
2. Visualizar tarefas
3. Concluir tarefa
4. Remover tarefa
5. Sair

Escolha uma opção: 1
Título: Estudar Python
Descrição: Revisar funções e listas
Prioridade (Alta, Média ou Baixa): Media
Data limite (DD/MM/AAAA): 20/10/2026
Tarefa "Estudar Python" cadastrada com sucesso!
```

Ao visualizar, o programa exibe os dados da tarefa e o resumo:

```text
========== RESUMO ==========

Total de tarefas: 1
Pendentes: 1
Concluídas: 0
```

## Regras de validação

| Código | Regra implementada |
|---|---|
| R01 | O título é obrigatório, tem espaços externos removidos e não pode conter somente espaços. |
| R02 | A prioridade aceita somente Alta, Média/Media ou Baixa, sem diferenciar maiúsculas e minúsculas. |
| R03 | A data deve existir e usar exatamente o formato DD/MM/AAAA. |
| R04 | Cada tarefa recebe um ID numérico único, que não é reutilizado durante a execução. |
| R05 | Toda tarefa começa com o status `Pendente`. |
| R06 | Somente tarefas existentes e pendentes podem ser concluídas. |
| R07 | A remoção mostra o título e exige confirmação `S`. |
| R08 | Uma lista vazia produz uma mensagem clara. |
| R09 | Uma opção inválida exibe um erro e retorna ao menu sem perder dados. |

IDs não numéricos também são tratados sem encerrar inesperadamente a aplicação.

## Testes

A suíte automatizada cobre os 18 cenários definidos para menu, cadastro,
validações, listagem, IDs, conclusão, remoção e encerramento. Para executá-la na
raiz do projeto:

```bash
python -m unittest discover -s tests -v
```

No Linux ou macOS, use `python3` se esse for o nome do executável.

## Relação com a Fase 1

O arquivo [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf) é a
cópia fiel do planejamento entregue na Fase 1. O código traduz a receita lógica
desse documento em funções Python, uma lista de dicionários e um laço contínuo
de menu. Embora o enunciado mínimo da Fase 2 apresente três opções, foram
mantidas as cinco operações planejadas originalmente para preservar a evolução
cumulativa do TaskTracker.

## Evolução na Fase 3

A Fase 3 adiciona o `Dockerfile`, a configuração do Docker Compose e as
instruções de execução em contêiner, preservando o planejamento da Fase 1, o
código Python e as regras de negócio da Fase 2. O escopo continua sendo uma CLI
em memória: não foram adicionados banco de dados, servidor HTTP ou frameworks.

## Identificação acadêmica

- **Estudante:** Vinícius Cesar Sena Torres
- **Curso:** Ciência de Dados e Machine Learning
- **Turma/Polo:** Turma B — Asa Norte
- **Disciplina:** Bootcamp II
- **Modalidade:** EAD
