contas = [
    {
        "user": "admin",
        "tarefas": [
            {
                "nome": "Limpar janelas",
            }
        ]
    },
    {
        "user": "Robot",
        "tarefas": [
            {
                "nome": "Organizar quarto",
            }
        ]
    }
]

userAtual = ""

def apresentarOp():
    opcao = input("Diga o que quer fazer agora(addTask, showTasks, login, create_user): ")
    opcoes(opcao)

def opcoes(op):
    global userAtual
    if op == "addTask":
        nameTask = input("Digite o nome de sua nova tarefa: ")
        for conta in contas:
            if conta['user'] == userAtual:
                novaTarefa = {"nome": nameTask}
                conta['tarefas'].append(novaTarefa)
                apresentarOp()
    elif op == "showTasks":
        for conta in contas:
            if conta['user'] == userAtual:
                for tarefa in conta["tarefas"]:
                    print(f"    -> {tarefa['nome']}")
                apresentarOp()
    elif op == "login":
        login()
    elif op == "create_user":
        nameNewUser = input("Digite o novo nome do usuario: ")
        novaConta = {"user": nameNewUser, "tarefas": []}
        contas.append(novaConta)
        print("Agora faça login!")
        login()
    else:
        print("Comando Invalido!")
        apresentarOp()

def login():
    global userAtual
    userI = input("Digite o nome do seu usuario: ")
    for user in contas:
        if userI in user['user']:
            userAtual = userI
            print(f"logado como {userAtual}")
            apresentarOp()

login()