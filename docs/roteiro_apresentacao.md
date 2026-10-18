# Roteiro de apresentação — TaskTracker

**Duração-alvo:** aproximadamente 5 minutos  
**Formato:** horizontal 16:9, com webcam e voz do estudante  
**Apresentador:** Vinícius Cesar Sena Torres

## 0:00–0:30 — Apresentação e contexto

> Olá, meu nome é Vinícius Cesar Sena Torres, sou estudante de Ciência de Dados
> e Machine Learning, da Turma B, polo Asa Norte. Este é o TaskTracker, projeto
> da Fase 2 do Bootcamp II. Nesta etapa, transformei o planejamento lógico da
> Fase 1 em uma aplicação Python funcional executada pelo terminal.

Mantenha a webcam visível e apresente rapidamente o objetivo: organizar tarefas
pessoais, prioridades e prazos.

## 0:30–2:00 — GitHub, estrutura e histórico

Abra o repositório publicado no GitHub e mostre:

1. a raiz com `README.md`, `.gitignore`, `docs`, `src` e `tests`;
2. `docs/planejamento_logico.pdf`, explicando que é o documento original da
   Fase 1 preservado para rastreabilidade;
3. `src/main.py`, que contém o menu, as operações e as validações;
4. `tests/test_main.py`, com os cenários automatizados;
5. o README, destacando execução, regras R01–R09 e próximos passos;
6. o histórico com os quatro commits, explicando brevemente a evolução real:
   estrutura, funcionalidades, validações/testes e documentação.

Frase sugerida:

> O histórico foi dividido em commits coerentes para mostrar a evolução do
> projeto, desde a estrutura inicial até as regras de negócio e a documentação.

## 2:00–4:00 — Demonstração prática

Na raiz do projeto, execute:

```bash
python src/main.py
```

Faça a demonstração nesta ordem:

1. escolha `1` para cadastrar;
2. pressione Enter com o título vazio para mostrar a validação R01;
3. digite `Estudar Python` como título;
4. informe `Revisar funções e listas` como descrição;
5. digite uma prioridade inválida, como `Urgente`, para mostrar a validação R02;
6. corrija para `Media` e explique a normalização para `Média`;
7. informe primeiro `31/02/2026`, mostre a rejeição e corrija para uma data real;
8. escolha `2` e mostre todos os campos e o resumo;
9. se houver tempo, escolha `3`, conclua o ID `1` e liste novamente.

Explique durante a execução:

> As tarefas ficam em uma lista de dicionários apenas durante a execução. Cada
> uma recebe ID único e status inicial Pendente. As entradas inválidas não
> encerram o programa nem apagam as tarefas já cadastradas.

## 4:00–4:30 — Encerramento e Fase 3

> O TaskTracker agora atende às regras planejadas, possui testes automatizados e
> está versionado de forma rastreável. Na Fase 3, o próximo passo será empacotar
> a aplicação com Docker, ampliar os testes e preparar o deploy conforme o novo
> enunciado. Obrigado.

## 4:30–5:00 — Margem de gravação

Use os segundos restantes para transições entre GitHub, editor e terminal ou
para mostrar o comando dos testes:

```bash
python -m unittest discover -s tests -v
```

Antes de publicar, confirme que o vídeo está em 16:9, dura aproximadamente cinco
minutos, mantém rosto e voz próprios e está como **Público** ou **Não listado**.
