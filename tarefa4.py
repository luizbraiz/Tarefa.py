# Abre o arquivo no modo ’w’ para comecar uma lista nova
with open (" tarefas .txt ", "w") as arquivo_tarefas :
    print (" Por favor , digite 3 tarefas a serem feitas :")
for i in range (3) :
    tarefa = input ( f" Tarefa {i + 1}: ")
arquivo_tarefas . write ( tarefa + "\n")

print ("\ nLista de tarefas foi salva em ’tarefas .txt ’!")