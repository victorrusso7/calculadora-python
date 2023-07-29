# Passo 1: Criar uma classe para representar uma conta bancária.
class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def verificar_saldo(self):
        print(f"Saldo atual de {self.nome}: R${self.saldo:.2f}")


# Passo 2: Função principal do sistema bancário.
def main():
    # Dicionário para armazenar contas bancárias com base nos nomes dos clientes.
    contas = {}

    while True:
        print("\n===== Bem-vindo ao Sistema Bancário =====")
        print("1. Criar uma nova conta")
        print("2. Acessar uma conta existente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_cliente = input("Digite o nome do cliente: ")
            saldo_inicial = float(input("Digite o saldo inicial: "))
            contas[nome_cliente] = ContaBancaria(nome_cliente, saldo_inicial)
            print("Conta criada com sucesso!")

        elif opcao == "2":
            nome_cliente = input("Digite o nome do cliente: ")
            if nome_cliente in contas:
                conta_atual = contas[nome_cliente]
                print(f"Bem-vindo(a), {nome_cliente}!")
                while True:
                    print("\n1. Depositar dinheiro")
                    print("2. Sacar dinheiro")
                    print("3. Verificar saldo")
                    print("4. Voltar ao menu principal")
                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == "1":
                        valor_deposito = float(input("Digite o valor a depositar: "))
                        conta_atual.depositar(valor_deposito)
                        print("Depósito realizado com sucesso!")

                    elif opcao_conta == "2":
                        valor_saque = float(input("Digite o valor a sacar: "))
                        conta_atual.sacar(valor_saque)

                    elif opcao_conta == "3":
                        conta_atual.verificar_saldo()

                    elif opcao_conta == "4":
                        break

                    else:
                        print("Opção inválida!")

            else:
                print("Cliente não encontrado. Crie uma conta primeiro.")

        elif opcao == "3":
            print("Sistema encerrado. Até logo!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
