# Roteiro de apresentação — TaskTracker — Fase 3

## Preparação antes de gravar

- Grave em formato horizontal 16:9, com seu rosto visível e sua própria voz.
- Deixe o repositório, o terminal e o README abertos antes de iniciar.
- Confirme que o Docker Desktop está em execução e faça o build antes da
  gravação, se quiser evitar espera durante o vídeo.
- Publique o vídeo no YouTube como **Público** ou **Não listado**, nunca como
  Privado.

## 0:00–0:30 — Apresentação do estudante e do projeto

Mantenha a câmera visível e diga:

> Olá, meu nome é Vinícius Cesar Sena Torres, sou estudante de Ciência de Dados
> e Machine Learning, da Turma B, polo Asa Norte. Este é o TaskTracker, projeto
> desenvolvido ao longo do Bootcamp II. Na Fase 3, containerizei a aplicação
> Python para que ela rode de forma reproduzível e interativa com Docker.

Resuma o objetivo: cadastrar, listar, concluir e remover tarefas pessoais por
meio de um menu no terminal.

## 0:30–1:30 — Repositório, histórico e novos arquivos

Mostre a raiz do repositório e destaque que o histórico das fases anteriores foi
preservado. Abra rapidamente:

1. `docs/planejamento_logico.pdf`, planejamento original da Fase 1;
2. `src/main.py`, implementação e regras de negócio da Fase 2;
3. `Dockerfile`, `docker-compose.yml` e a nova seção do `README.md`;
4. `docs/roteiro_fase3.md`.

No terminal, execute `git log --oneline` e explique que os novos commits separam
containerização, orquestração e documentação.

## 1:30–2:30 — Dockerfile e interatividade com Docker Compose

Abra o `Dockerfile` e explique cada linha:

- `FROM python:3.11-slim`: base Python leve;
- `WORKDIR /app`: diretório de trabalho do contêiner;
- `PYTHONUNBUFFERED=1`: imprime as mensagens imediatamente;
- `COPY src/ /app/src/`: copia apenas o código necessário;
- `CMD ["python", "src/main.py"]`: inicia o TaskTracker.

Depois mostre `docker-compose.yml`. Explique que `stdin_open: true` mantém o
canal de entrada aberto e `tty: true` cria um terminal virtual. As duas opções
são necessárias porque o programa usa `input()` para interagir com o usuário.

## 2:30–4:30 — Demonstração prática

Na raiz do projeto, mostre o build:

```bash
docker build -t tasktracker .
```

Execute diretamente com Docker:

```bash
docker run -it --rm tasktracker
```

No menu, faça esta sequência:

1. digite `1` para cadastrar uma tarefa;
2. pressione Enter com o título vazio e mostre a rejeição;
3. informe `Estudar Docker` como título;
4. informe `Revisar containerização` como descrição;
5. digite `Urgente` e mostre a rejeição da prioridade inválida;
6. corrija para `Alta`;
7. informe uma data válida no formato `DD/MM/AAAA`;
8. escolha `2` e mostre a tarefa na listagem;
9. escolha `5` e confirme o encerramento normal.

Em seguida, demonstre a execução pelo serviço do Compose:

```bash
docker compose run --rm tasktracker
```

Mostre o menu, explique que a configuração de interatividade foi aplicada pelo
Compose e escolha `5` para encerrar. Compare: `docker run` usa diretamente a
imagem; o Compose usa a configuração declarativa do serviço `tasktracker`.

## 4:30–5:00 — Conclusão e evolução do projeto

Diga:

> O TaskTracker evoluiu do planejamento lógico para uma aplicação Python e,
> agora, para uma imagem Docker leve e reproduzível. O histórico e as regras de
> negócio foram preservados, e a configuração do Compose garante a interação
> correta com o menu. Obrigado.

Mostre por alguns segundos o README com os três comandos de execução.

## Checklist antes de publicar

- duração aproximada de 5 minutos;
- vídeo horizontal em 16:9;
- rosto visível e voz própria durante a apresentação;
- build, `docker run -it` e Docker Compose demonstrados;
- cadastro, título vazio, prioridade inválida e listagem demonstrados;
- vídeo no YouTube como **Público** ou **Não listado**;
- link ativo do GitHub e link ativo do YouTube inseridos no PDF final do AVA.
