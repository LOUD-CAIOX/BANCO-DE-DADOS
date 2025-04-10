import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("Bem-vindo ao menu de cadastros")
    print("1 - Novo cadastro")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("4 - Atualizar cadastro")
    print("5 - Deletar cadastro") 
    print("----------------------")

def salvar (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def cadastrar_pessoa(cadastros):
    nome = input("Nome: ")
    idade = input("Idade: ")
    turma = input("Turma: ")
    curso = input("Curso: ")
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    salvar(cadastros)
    print("Cadastro finalizado com sucesso")

def ver_cadastros(cadastros):
    if not cadastros:
        print("Nenhum cadastro no sistema")
    else:
        print("\n-------Lista de Cadastros------")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i} . Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")

def atualizar_cadastro(cadastros):
    if not cadastros:
        print("Nenhum cadastro disponível para atualizar.")
        return

    ver_cadastros(cadastros)
    try:
        indice = int(input("Digite o número do cadastro que deseja atualizar: ")) - 1
        if 0 <= indice < len(cadastros):
            print("Deixe em branco se não quiser alterar o campo.")
            nome = input(f"Novo nome (atual: {cadastros[indice]['Nome']}): ") or cadastros[indice]['Nome']
            idade = input(f"Nova idade (atual: {cadastros[indice]['Idade']}): ") or cadastros[indice]['Idade']
            turma = input(f"Nova turma (atual: {cadastros[indice]['Turma']}): ") or cadastros[indice]['Turma']
            curso = input(f"Novo curso (atual: {cadastros[indice]['Curso']}): ") or cadastros[indice]['Curso']

            cadastros[indice] = {"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso}
            salvar(cadastros)
            print("Cadastro atualizado com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def deletar_cadastro(cadastros):
    if not cadastros:
        print("Nenhum cadastro disponível para deletar.")
        return

    ver_cadastros(cadastros)
    try:
        indice = int(input("Digite o número do cadastro que deseja deletar: ")) - 1
        if 0 <= indice < len(cadastros):
            confirmacao = input(f"Tem certeza que deseja deletar {cadastros[indice]['Nome']}? (s/n): ").lower()
            if confirmacao == "s":
                removido = cadastros.pop(indice)
                salvar(cadastros)
                print(f"Cadastro de {removido['Nome']} deletado com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

def main():
    cadastros = carregar_cadastros()
    while True:
        exibir_menu()
        opção = input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa(cadastros)
        elif opção == "2":
            ver_cadastros(cadastros)
        elif opção == "3":
            print("Obrigado por usar o sistema! Até logo!")
            break
        elif opção == "4":
            atualizar_cadastro(cadastros)
        elif opção == "5":
            deletar_cadastro(cadastros)
        else:
            print("Escolha entre 1, 2, 3, 4 ou 5.")


if __name__ == "__main__":
    main()

