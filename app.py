def add_lead():
    print("Lead adicionado (func)")


def main():

    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Sair do programa")

        opt = input("Escolha uma opção")

        if opt == "1":
            print("Lead adicionado")
        elif opt == "2":
            print("Listar leads")
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()