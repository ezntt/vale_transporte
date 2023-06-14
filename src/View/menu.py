class MenuView:

    def print_data(self, message):
        print(message)

    def show_options(self):
        while True:
            print("Escolha uma opção:")
            print("1. Adicionar funcionário")
            print("2. Adicionar usuário")
            print("3. Sair")

            opcao = input("Opção: ")

            if opcao == "1" or opcao == "2":
                return opcao
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")
