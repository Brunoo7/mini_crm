from model import model_lead

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    status = input("Etapa no funil de vendas: ")

    model_lead(name, email, status)

    print("Lead adicionado (func)")


def main():

    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Listar leads")
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()