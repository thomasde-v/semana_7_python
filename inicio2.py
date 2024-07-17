from funçoes import soma_dois_numeros, mutiplicaçao_dois_numeros, divisao_dois_numeros, subtraçao_dois_numeros

def exibir_menu():
    print("\n=== MENU ====")
    print("1. Somar números")
    print("2. Subtrair números")
    print("3. Multiplicar números")
    print("4. Dividir números")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1 a 5): ")

        if escolha == "1":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            resultado_soma = soma_dois_numeros(n1, n2)
            print(f"A soma de {n1} e {n2} é igual a {resultado_soma}")

        elif escolha == "2":
            n9 = float(input("Digite o primeiro número: "))
            n10 = float(input("Digite o segundo número: "))
            resultado_subtracao = subtraçao_dois_numeros(n9, n10)
            print(f"A subtração de {n9} e {n10} é igual a {resultado_subtracao}")

        elif escolha == "3":
            n3 = float(input("Digite o primeiro número: "))
            n4 = float(input("Digite o segundo número: "))
            resultado_multiplicacao = mutiplicaçao_dois_numeros(n3, n4)
            print(f"A multiplicação de {n3} e {n4} é igual a {resultado_multiplicacao}")

        elif escolha == "4":
            n7 = float(input("Digite o primeiro número: "))
            n8 = float(input("Digite o segundo número: "))
            resultado_divisao = divisao_dois_numeros(n7, n8)
            print(f"A divisão de {n7} e {n8} é igual a {resultado_divisao}")

        elif escolha == "5":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
