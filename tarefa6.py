# Abre o arquivo no modo ’w’ ( write / escrita )
with open (" meu_diario .txt ", "w") as diario :
 diario . write ("Hoje , 03 de outubro de 2025 , comecei meu diariodigital .\n")
print (" Arquivo meu_diario .txt ","criado com sucesso !" )
try:
# Abre o arquivo no modo ’r’ ( read / leitura )
    with open (" meu_diario .txt ", "r") as diario :
        conteudo = diario . read ()
        print (" --- Conteudo do Diario ---")
        print ( conteudo )
except FileNotFoundError :
    print ("O arquivo ’meu_diario .txt ’ ainda nao existe . Rode oexercicio 1 primeiro .")
    # Abre o arquivo no modo ’a’ ( append / anexar )
with open (" meu_diario .txt ", "a") as diario :
    diario . write (" Estou aprendendo a manipular arquivos e e muito util.\n")

print (" Novo pensamento adicionado ao diario !")
# Abre o arquivo no modo ’w’ para comecar uma lista nova
with open (" tarefas .txt ", "w") as arquivo_tarefas :
    print (" Por favor , digite 3 tarefas a serem feitas :")
for i in range (3) :
    tarefa = input ( f" Tarefa {i + 1}: ")
arquivo_tarefas . write ( tarefa + "\n")

print ("\ nLista de tarefas foi salva em ’tarefas .txt ’!")
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