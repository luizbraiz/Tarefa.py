print (" --- Minha Lista de Tarefas ---")
try:
    with open (" tarefas .txt ", "r") as arquivo_tarefas :
        numero_tarefa = 1
        for tarefa in arquivo_tarefas :
            # O f- string ajuda a formatar a saida
            print ( f"{ numero_tarefa }. { tarefa . strip ()}")
            numero_tarefa += 1 # O mesmo que numero_tarefa =
    numero_tarefa + 1
except FileNotFoundError :
    print (" Arquivo ’tarefas .txt ’ nao encontrado . Rode o exercicio 4primeiro .")